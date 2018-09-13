# -*- coding: utf-8 -*-
# Copyright (c) 2013, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.pdf import get_pdf


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
    # get columns
    columns = get_columns()

    return columns, data


@frappe.whitelist()
def download_pdf_csv(name):
    data = execute(name, csv=True)
    return data


@frappe.whitelist()
def download_pdf_pnd(name):
    columns, data = execute(name)
    content = frappe.render_template(
        'thai_wht/thai_wht/report/pnd_attach/pnd_attach.html',
        {
            'data': data,
            'columns': columns,
        }
        )
    html = frappe.render_template(
        'public/html/print_template_pnd.html',
        {
            'content': content,
            'title': name,
            'landscape ': True,
            'print_settings': {},
            'columns': columns,
        }
    )
    frappe.local.response.filename = '{name}.pdf'.format(
        name=name.replace(' ', '-').replace('/', '-')
        )
    frappe.local.response.filecontent = get_pdf(
        html,
        {'orientation': 'Landscape'}
        )
    frappe.local.response.type = 'download'


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
    pnd_dict['_date'] = 'วันที่ {:02d} เดือน {} พ.ศ. {}'.format(
        pnd_dict.date.day,
        thai_month[pnd_dict.date.month-1],
        pnd_dict.date.year+543
        )
    
    id = pnd_dict.whder
    pnd_dict['_whder'] = '{}-{}-{}-{}-{}'.format(
        id[0], id[1:5], id[5:10], id[10:12], id[12]
        )
    
    return pnd_dict


def get_page_and_total(data):
    total = {}

    # cal page
    line_in_page = 6
    line_left = len(data) % line_in_page
    pages = len(data) // line_in_page
    if line_left > 0:
        pages += 1
    total['pages'] = pages
    total['line_left'] = line_left
    total['line_in_page'] = line_in_page

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
                    page_wht += int(data[item]['{}{}'.format('wht', i)])
                except KeyError:
                    pass
                try:
                    page_paid += int(data[item]['{}{}'.format('paid', i)])
                except KeyError:
                    pass

        _page_wht = '{:,.2f}'.format(page_wht)
        _page_paid = '{:,.2f}'.format(page_paid)

        total[page] = {}
        total[page]['wht'] = page_wht
        total[page]['paid'] = page_paid
        total[page]['_wht'] = _page_wht
        total[page]['_paid'] = _page_paid

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
