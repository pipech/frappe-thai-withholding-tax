# -*- coding: utf-8 -*-
# Copyright (c) 2013, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import os
import pdfkit

from frappe.utils.pdf import prepare_options
from frappe.utils import scrub_urls
from thai_wht.thai_wht.report.pnd_attach.pnd_attach import execute
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter


@frappe.whitelist()
def download(name):
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
