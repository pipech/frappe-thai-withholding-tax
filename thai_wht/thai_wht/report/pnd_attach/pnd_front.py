from __future__ import unicode_literals

import frappe
import os
import pdfkit
import StringIO

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileWriter


@frappe.whitelist()
def download_pdf_pnd():

    # tempory file name
    hash_name = frappe.generate_hash()
    fname_merged = os.path.join(
        '/tmp',
        'pnd-{0}.pdf'.format(hash_name)
        )
    fname_fill = os.path.join(
        '/tmp',
        'pnd-fill-{0}.pdf'.format(hash_name)
        )

    # generate pnd fill layer
    html = '<h1>Is this a book</h1>'
    pdfkit.from_string(
        input=html,
        output_path=fname_fill,
        options={'orientation': 'Portrait'}
        )

    # read pdf
    existing_pdf = PdfFileReader('assets/thai_wht/pnd_template/pnd3.pdf')
    new_pdf = PdfFileReader(fname_fill)

    # merge pdf
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output = PdfFileWriter()
    output.addPage(page)

    # finally, write 'output' to a real file
    outputStream = open(fname_merged, 'wb')
    output.write(outputStream)
    outputStream.close()

    # get read file to use for frappe response
    with open(fname_merged, 'rb') as fileobj:
        filedata = fileobj.read()

    # delete tempory file
    if os.path.exists(fname_merged):
        os.remove(fname_merged)
    if os.path.exists(fname_fill):
        os.remove(fname_fill)

    # respond
    frappe.local.response.filename = 'aaaa.pdf'
    frappe.local.response.filecontent = filedata
    frappe.local.response.type = 'download'
