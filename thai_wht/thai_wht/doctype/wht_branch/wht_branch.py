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

        if self.zip_code:
            try:
                int(self.zip_code)
            except ValueError:
                frappe.throw('รหัสไปรษณีย์ไม่ถูกต้อง กรุณากรอกรหัสไปรษณีย์เป็นตัวเลข')

            if len(self.zip_code) != 5:
                frappe.throw('รหัสไปรษณีย์ไม่ถูกต้อง กรุณากรอกรหัสไปรษณีย์เป็นตัวเลข 5 หลัก')


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
def get_branch_display(branch_dict, oneline=False):
    if not branch_dict:
        return

    if not isinstance(branch_dict, dict):
        branch_dict = frappe.db.get_value(
            'Wht Branch', branch_dict, '*', as_dict=True
            ) or {}

    template = """
        {{ address_line1 }}
        {% if moo %}ม.{{ moo }}{% endif %}
        {% if road %}ถ.{{ road }}{% endif %}
        {% if soi %}ซ.{{ soi }}{% endif %}
        {% if sub_soi %}แยก{{ sub_soi }}{% endif %}
        {% if moo_ban %}หมู่บ้าน{{ moo_ban }}{% endif %}
        <br>
        {% if building %}
            อาคาร{{ building }}
            {% if floor_no %}ชั้นที่{{ floor_no }}{% endif %}
            {% if room_no %}ห้องที่{{ room_no }}{% endif %}
            <br>
        {% endif %}
        {% if province == 'กรุงเทพมหานคร' %}
            แขวง{{ sub_district }} เขต{{ district }}<br>
            {{ province }}<br>
        {% else %}
            ต.{{ sub_district }} อ.{{ district }}<br>
            จ.{{ province }}<br>
        {% endif %}
        {% if zip_code %}
            {{ zip_code }}<br>
        {% endif %}
    """

    if oneline:
        template = template.replace('<br>', '')
        template = ' '.join(template.split())

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

    addr = get_branch_display(branch_dict, oneline=True)

    branch_dict.address = addr

    return branch_dict
