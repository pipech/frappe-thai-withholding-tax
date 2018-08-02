# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import load_address_and_contact
from thai_wht.thai_wht.thai_utils import check_tax_id


class Whdee(Document):
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
        load_address_and_contact(self)
