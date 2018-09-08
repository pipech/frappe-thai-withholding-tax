# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from thai_wht.thai_wht.thai_utils import check_tax_id
from thai_wht.thai_wht.doctype.wht_branch.wht_branch import load_branch


class Whder(Document):
    def before_insert(self):
        if self.whder_no is None:
            total_whder_sql = frappe.db.sql(
                'SELECT COUNT(*) AS "total" FROM `tabWhder`;',
                as_dict=1
            )
            total_whder = total_whder_sql[0].total
            if total_whder <= 10:
                self.whder_no = total_whder
            else:
                frappe.throw('ไม่สามารถสร้าง ผู้มีหน้าที่หักภาษี ณ ที่จ่าย เกิน 10 ราย')

    def before_save(self):
        self.type = frappe.get_value('Prefix', self.prefix, 'type')
        # remove duplicated spaces
        self.w_name = ' '.join(self.w_name.split())

    def validate(self):
        self.tax_id = self.tax_id.replace(' ', '-')
        self.name = self.tax_id.replace('-', '')
        if not check_tax_id(self.name):
            frappe.throw('เลขบัตรประจำตัวประชาชน ไม่ถูกต้อง')

    def onload(self):
        load_branch(self)
