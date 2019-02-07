# -*- coding: utf-8 -*-
# Copyright (c) 2013, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import os

from thai_wht.thai_wht.report.pnd_attach.pnd_paper import pnd_gen_pdf
from thai_wht.thai_wht.doctype.wht_branch.wht_branch import get_branch_address


@frappe.whitelist()
def print_envelope(name):
    # get data
    wht_cert = frappe.get_doc('Wht Cert', name).as_dict()
    print(wht_cert)

    # get addr
    whder_addr = get_branch_address(
        wht_cert.get('whder_branch'),
        oneline=False
        )
    whdee_addr = get_branch_address(
        wht_cert.get('whdee_branch'),
        oneline=False
        )

    # prepared html
    env_html = frappe.render_template(
        'thai_wht/templates/includes/pnd_envelope.html',
        {
            'data': wht_cert,
            'whder_addr': whder_addr.address,
            'whdee_addr': whdee_addr.address,
        }
        )

    # temp file name
    hash_name = frappe.generate_hash()
    fname_attach = os.path.join(
        '/tmp',
        'pnd-attach-{0}.pdf'.format(hash_name)
        )

    # generate pdf
    # envelope size 108x235mm
    pnd_gen_pdf(
        html=env_html,
        options={
            'page-height': 108,
            'page-width': 235,
        },
        output_path=fname_attach,
    )

    # get read file to use for frappe response
    fileobj = open(fname_attach, 'rb')
    filedata = fileobj.read()
    fileobj.close()

    # delete temp file
    if os.path.exists(fname_attach):
        os.remove(fname_attach)

    # frappe response
    frappe.local.response.filename = '{name}.pdf'.format(
        name=name.replace(' ', '-').replace('/', '-')
        )
    frappe.local.response.filecontent = filedata
    frappe.local.response.type = 'download'
