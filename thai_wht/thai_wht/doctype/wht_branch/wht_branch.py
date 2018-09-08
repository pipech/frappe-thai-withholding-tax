# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class WhtBranch(Document):
    def before_save(self):
        # fill branch with leading 5 zeros
        self.branch = self.branch.zfill(5)
        # remove duplicated spaces
        self.address_line1 = ' '.join(self.address_line1.split())

    def validate(self):
        if self.branch is None:
            self.branch = '0'
        try:
            int(self.branch)
        except ValueError:
            frappe.throw('สาขาไม่ถูกต้อง กรุณากรอกสาขาเป็นตัวเลข')


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


@frappe.whitelist()
def get_branch_select(link_doctype, link_name):
    filters = [
        ['Dynamic Link', 'link_doctype', '=', link_doctype],
        ['Dynamic Link', 'link_name', '=', link_name],
        ['Dynamic Link', 'parenttype', '=', 'Wht Branch'],
    ]
    branch_list = frappe.get_all(
        'Wht Branch',
        filters=filters,
        fields=['*'],
        order_by='branch asc'
        )
    return branch_list


def get_branch_address(branch):
    branch_dict = frappe.get_value(
        'Wht Branch', branch, '*', as_dict=True
        )

    if branch_dict == 'กรุงเทพมหานคร':
        addr_temp = '{addr} แขวง{sub_district} เขต{district} {province}'
    else:
        addr_temp = '{addr} ต.{sub_district} อ.{district} จ.{province}'

    branch_dict.address = addr_temp.format(
        addr=branch_dict.address_line1,
        sub_district=branch_dict.sub_district,
        district=branch_dict.district,
        province=branch_dict.province,
        )

    return branch_dict
