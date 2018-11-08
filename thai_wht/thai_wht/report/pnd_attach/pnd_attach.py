# -*- coding: utf-8 -*-
# Copyright (c) 2013, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import os
import pdfkit

from decimal import Decimal
from frappe.utils import scrub_urls
from frappe.utils.pdf import prepare_options
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileWriter


def execute(name, csv=False, filters=None):
    # get raw data
    data = get_data(name)
    # format and arrange data
    data = arrange_data(data)
    if csv:
        return data
    data = format_data(data)
    # adding additional data
    if name:
        data[0]['pnd'] = get_pnd(name)
        data[0]['total'] = get_page_and_total(data)
        data[0]['total']['all'] = \
            data[0]['total']['all_wht'] + data[0]['pnd']['penalty']
        data[0]['total']['_all'] = '{:,.2f}'.format(data[0]['total']['all'])
    # get columns
    columns = get_columns()

    return columns, data


@frappe.whitelist()
def download_pdf_csv(name):
    data = execute(name, csv=True)
    return data


@frappe.whitelist()
def download_pdf_pnd(name):
    # get data
    columns, data = execute(name)
    pnd = data[0]['pnd']['pnd']

    # prepared html
    content_attach = frappe.render_template(
        'thai_wht/thai_wht/report/pnd_attach/pnd_attach.html',
        {
            'data': data,
            'columns': columns,
        }
        )
    html_attach = frappe.render_template(
        'public/html/print_template_pnd.html',
        {
            'content': content_attach,
            'title': name,
            'landscape ': True,
            'print_settings': {},
            'columns': columns,
        }
    )
    content_front = frappe.render_template(
        'thai_wht/thai_wht/report/pnd_attach/pnd_front_{}.html'.format(pnd),
        {
            'data': data,
            'columns': columns,
        }
        )
    html_front = frappe.render_template(
        'public/html/print_template_pnd_front.html',
        {
            'content': content_front,
            'title': name,
            'landscape ': False,
            'print_settings': {},
            'columns': columns,
        }
    )

    # temp file name
    hash_name = frappe.generate_hash()
    fname_merged = os.path.join(
        '/tmp',
        'pnd-{0}.pdf'.format(hash_name)
        )
    fname_attach = os.path.join(
        '/tmp',
        'pnd-attach-{0}.pdf'.format(hash_name)
        )
    fname_front_merged = os.path.join(
        '/tmp',
        'pnd-front-merged-{0}.pdf'.format(hash_name)
        )
    fname_front = os.path.join(
        '/tmp',
        'pnd-front-{0}.pdf'.format(hash_name)
        )

    # generate pdf
    pnd_gen_pdf(
        html=html_attach,
        options={'orientation': 'Landscape'},
        output_path=fname_attach,
    )
    pnd_gen_pdf(
        html=html_front,
        options={'orientation': 'Portrait'},
        output_path=fname_front,
    )

    # read front template
    pdf_template = PdfFileReader('assets/thai_wht/pnd_template/pnd{}.pdf'.format(pnd))
    pdf_front = PdfFileReader(fname_front)

    # merge front page
    front_page = pdf_template.getPage(0)
    front_page.mergePage(pdf_front.getPage(0))
    output = PdfFileWriter()
    output.addPage(front_page)

    # write output to pdf file
    outputStream = open(fname_front_merged, 'wb')
    output.write(outputStream)
    outputStream.close()

    # merged front and attach pdf
    # open file
    front_merged_stream = open(fname_front_merged, 'rb')
    attach_stream = open(fname_attach, 'rb')
    # import_bookmarks is here to prevent error
    # "utils.PdfReadError("Unexpected destination %r" % dest)"
    # https://github.com/mstamy2/PyPDF2/issues/193
    # merge file
    merger = PdfFileMerger()
    merger.append(front_merged_stream, import_bookmarks=False)
    merger.append(attach_stream, import_bookmarks=False)
    merger.write(fname_merged)
    # close file
    front_merged_stream.close()
    attach_stream.close()

    # get read file to use for frappe response
    fileobj = open(fname_merged, 'rb')
    filedata = fileobj.read()
    fileobj.close()

    # delete temp file
    if os.path.exists(fname_merged):
        os.remove(fname_merged)
    if os.path.exists(fname_attach):
        os.remove(fname_attach)
    if os.path.exists(fname_front_merged):
        os.remove(fname_front_merged)
    if os.path.exists(fname_front):
        os.remove(fname_front)

    # frappe response
    frappe.local.response.filename = '{name}.pdf'.format(
        name=name.replace(' ', '-').replace('/', '-')
        )
    frappe.local.response.filecontent = filedata
    frappe.local.response.type = 'download'


def pnd_gen_pdf(html, options, output_path):
    html = scrub_urls(html)
    html, options = prepare_options(html, options)
    pdfkit.from_string(
        input=html,
        output_path=output_path,
        options=options
        )


def format_data(data):
    for d in data:
        for i in range(3):
            # format date
            try:
                d['_{}{}'.format('date', i)] = '{:02d}/{:02d}/{}'.format(
                    d['{}{}'.format('date', i)].day,
                    d['{}{}'.format('date', i)].month,
                    d['{}{}'.format('date', i)].year+543
                    )
            except KeyError:
                pass
            # format currency
            try:
                d['_{}{}'.format('paid', i)] = '{:,.2f}'.format(d['{}{}'.format('paid', i)])
                d['_{}{}'.format('wht', i)] = '{:,.2f}'.format(d['{}{}'.format('wht', i)])
            except KeyError:
                pass
        # format tax id
        id = d['whdee']
        d['_whdee'] = '{}-{}-{}-{}-{}'.format(
            id[0], id[1:5], id[5:10], id[10:12], id[12]
            )
    return data


def arrange_data(data):
    field = [
        'idx',
        'whdee',
        'whdee_branch_no',
        'whdee_prefix',
        'whdee_name',
        'whdee_branch_addr',
    ]
    detail_field = [
        'date',
        'type',
        'rate',
        'paid',
        'wht',
        'condition',
    ]
    pre_id = ''
    multiplier_num = 0
    data_list = []
    # loop through all data
    for d in data:
        cur_id = d['wht_cert_id']

        if pre_id == cur_id:
            multiplier_num += 1
        else:
            multiplier_num = 0
            new_row = {}
            # loop through all key if key is in field
            # then add data to new row
            for key, value in d.iteritems():
                if key in field:
                    new_row[key] = value

        for key, value in d.iteritems():
            if key in detail_field:
                k = '{k}{m}'.format(k=key, m=multiplier_num)
                new_row[k] = value

        if pre_id == cur_id:
            data_list.pop()

        data_list.append(new_row)

        pre_id = cur_id

    return data_list


def get_pnd(pnd_name):
    pnd_dict = frappe.get_value(
        doctype='Pnd',
        fieldname='*',
        filters=pnd_name,
        as_dict=1
        )

    thai_month = [
        'มกราคม',
        'กุมภาพันธ์',
        'มีนาคม',
        'เมษายน',
        'พฤษภาคม',
        'มิถุนายน',
        'กรกฎาคม',
        'สิงหาคม',
        'กันยายน',
        'ตุลาคม',
        'พฤศจิกายน',
        'ธันวาคม',
    ]
    pnd_dict['_date'] = '{:02d} เดือน {} พ.ศ. {}'.format(
        pnd_dict.date.day,
        thai_month[pnd_dict.date.month-1],
        pnd_dict.date.year+543
        )
    pnd_dict['year'] = int(pnd_dict['year'])

    pnd_dict['_penalty'] = '{:,.2f}'.format(pnd_dict['penalty'])
    pnd_dict['penalty'] = Decimal(pnd_dict['penalty'])

    id = pnd_dict.whder
    pnd_dict['_whder'] = '{}-{}-{}-{}-{}'.format(
        id[0], id[1:5], id[5:10], id[10:12], id[12]
        )
    pnd_dict['_whder_branch_no'] = ' '.join(pnd_dict['whder_branch_no'])
    pnd_dict['_whder1'] = id[0]
    pnd_dict['_whder2'] = ' '.join(id[1:5])
    pnd_dict['_whder3'] = ' '.join(id[5:10])
    pnd_dict['_whder4'] = ' '.join(id[10:12])
    pnd_dict['_whder5'] = ' '.join(id[12])

    return pnd_dict


def get_page_and_total(data):
    total = {}

    # cal page
    line_in_page = 6
    line_left = len(data) % line_in_page
    pages = len(data) // line_in_page
    if line_left > 0:
        pages += 1
    total['line'] = len(data)
    total['pages'] = pages
    total['line_left'] = line_left
    total['line_in_page'] = line_in_page

    all_wht = 0
    all_paid = 0

    # cal total
    for page in range(0, pages):
        page_wht = 0
        page_paid = 0

        # determine loop range
        if (page + 1) * line_in_page < len(data):
            end_data = (page + 1) * line_in_page
        else:
            end_data = len(data)
        start_data = page * line_in_page

        # loop cal total
        for item in range(start_data, end_data):
            for i in range(3):
                try:
                    page_wht += Decimal(data[item]['{}{}'.format('wht', i)])
                except KeyError:
                    pass
                try:
                    page_paid += Decimal(data[item]['{}{}'.format('paid', i)])
                except KeyError:
                    pass

        _page_wht = '{:,.2f}'.format(page_wht)
        _page_paid = '{:,.2f}'.format(page_paid)

        total[page] = {}
        total[page]['wht'] = page_wht
        total[page]['paid'] = page_paid
        total[page]['_wht'] = _page_wht
        total[page]['_paid'] = _page_paid

        all_wht += page_wht
        all_paid += page_paid

    total['all_wht'] = all_wht
    total['all_paid'] = all_paid

    total['_all_wht'] = '{:,.2f}'.format(all_wht)
    total['_all_paid'] = '{:,.2f}'.format(all_paid)

    return total


def get_data(name):

    sql_string = """
        SELECT

        `tabWht Cert`.`name` AS `wht_cert_id`,

        `tabWht Cert`.`whdee`,
        `tabWht Cert`.`whdee_prefix`,
        `tabWht Cert`.`whdee_name`,
        `tabWht Cert`.`whdee_branch_no`,
        `tabWht Cert`.`whdee_branch_addr`,

        `tabWht Cert Detail`.`date`,
        `tabWht Cert Detail`.`type`,
        `tabWht Cert Detail`.`rate`,
        `tabWht Cert Detail`.`paid`,
        `tabWht Cert Detail`.`wht`,
        `tabWht Cert Detail`.`condition`,

        `tabPnd Detail`.`idx`

        FROM `tabPnd`

        INNER JOIN `tabPnd Detail`
        ON `tabPnd Detail`.`parent`=`tabPnd`.`name`

        INNER JOIN `tabWht Cert`
        ON `tabWht Cert`.`name`=`tabPnd Detail`.`wht_cert`

        INNER JOIN `tabWht Cert Detail`
        ON `tabWht Cert Detail`.`parent`=`tabWht Cert`.`name`

        """

    if name:
        sql_string += 'WHERE `tabPnd`.`name`="{name}" '.format(
            name=name
            )
    else:
        sql_string += 'WHERE `tabPnd`.`owner`="{owner}" '.format(
            owner=frappe.session.user
            )

    sql_string += 'ORDER BY `tabPnd Detail`.`idx` ASC;'

    data = frappe.db.sql(sql_string, as_dict=1)

    return data


def get_columns():

    columns = [
        {
            'label': 'No',
            'fieldname': 'idx',
            'width': 20,
        },
        {
            'label': 'Tax Id',
            'fieldname': 'whdee',
            'width': 130,
        },
        {
            'label': 'Branch',
            'fieldname': 'whdee_branch_no',
            'width': 60,
        },
        {
            'label': 'Prefix',
            'fieldname': 'whdee_prefix',
            'width': 50,
        },
        {
            'label': 'Name',
            'fieldname': 'whdee_name',
            'width': 120,
        },
        {
            'label': 'Address',
            'fieldname': 'whdee_branch_addr',
            'width': 160,
        },
        {
            'label': 'Date',
            'fieldname': 'date0',
            'fieldtype': 'date',
        },
        {
            'label': 'Wht Type',
            'fieldname': 'type0',
            'width': 120,
        },
        {
            'label': 'Rate',
            'fieldname': 'rate0',
            'width': 40,
        },
        {
            'label': 'Paid',
            'fieldname': 'paid0',
            'fieldtype': 'Currency',
            'width': 90,
        },
        {
            'label': 'Wht',
            'fieldname': 'wht0',
            'fieldtype': 'Currency',
            'width': 90,
        },
        {
            'label': 'Condition',
            'fieldname': 'condition0',
            'width': 20,
        },
        {
            'label': 'Date',
            'fieldname': 'date1',
            'fieldtype': 'date',
        },
        {
            'label': 'Wht Type',
            'fieldname': 'type1',
            'width': 120,
        },
        {
            'label': 'Rate',
            'fieldname': 'rate1',
            'width': 40,
        },
        {
            'label': 'Paid',
            'fieldname': 'paid1',
            'fieldtype': 'Currency',
            'width': 90,
        },
        {
            'label': 'Wht',
            'fieldname': 'wht1',
            'fieldtype': 'Currency',
            'width': 90,
        },
        {
            'label': 'Condition',
            'fieldname': 'condition1',
            'width': 20,
        },
        {
            'label': 'Date',
            'fieldname': 'date2',
            'fieldtype': 'date',
        },
        {
            'label': 'Wht Type',
            'fieldname': 'type2',
            'width': 120,
        },
        {
            'label': 'Rate',
            'fieldname': 'rate2',
            'width': 40,
        },
        {
            'label': 'Paid',
            'fieldname': 'paid2',
            'fieldtype': 'Currency',
            'width': 90,
        },
        {
            'label': 'Wht',
            'fieldname': 'wht2',
            'fieldtype': 'Currency',
            'width': 90,
        },
        {
            'label': 'Condition',
            'fieldname': 'condition2',
            'width': 20,
        },
    ]

    return columns
