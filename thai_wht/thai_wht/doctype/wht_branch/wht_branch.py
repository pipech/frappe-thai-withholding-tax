# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class WhtBranch(Document):
    pass


def load_branch(doc):

    filters = [
        ['Dynamic Link', 'link_doctype', '=', doc.doctype],
        ['Dynamic Link', 'link_name', '=', doc.name],
        ['Dynamic Link', 'parenttype', '=', 'Wht Branch'],
    ]
    branch_list = frappe.get_all('Wht Branch', filters=filters, fields=['*'])

    branch_list = [
        a.update({'display': get_branch_display(a)})
        for a in branch_list
        ]

    doc.set_onload('branch_list', branch_list)


@frappe.whitelist()
def get_branch_display(branch_dict):
    if not branch_dict:
        return

    if not isinstance(branch_dict, dict):
        branch_dict = frappe.db.get_value(
            'Wht Branch', branch_dict, '*', as_dict=True
            ) or {}

    # with open('wht_branch_template.html', 'r') as template_file:
    #     template = template_file.read()

    template = """
        {% if province == 'กรุงเทพมหานคร' %}
            {{ address_line1 }}<br>
            แขวง{{ sub_district }} เขต{{ district }}<br>
            {{ province }}<br>
        {% else %}
            {{ address_line1 }}<br>
            ต.{{ sub_district }} อ.{{ district }}<br>
            จ.{{ province }}<br>
        {% endif %}
    """

    return frappe.render_template(template, branch_dict)
