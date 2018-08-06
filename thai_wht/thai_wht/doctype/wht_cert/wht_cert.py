# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from thai_wht.thai_wht.doctype.wht_branch.wht_branch import get_branch_address


class WhtCert(Document):
    def before_save(self):
        # get whder name and prefix
        whder = frappe.get_value(
            doctype='Whder',
            filters=self.whder,
            fieldname=['w_name', 'prefix'],
            as_dict=True,
            )
        self.whder_name = whder.w_name
        self.whder_prefix = whder.prefix
        # get whder branch
        whder_branch = get_branch_address(
            branch=self.whder_branch
            )
        self.whder_branch_no = whder_branch.branch
        self.whder_branch_addr = whder_branch.address

        # get whdee name and prefix
        whdee = frappe.get_value(
            doctype='Whdee',
            filters=self.whdee,
            fieldname=['w_name', 'prefix'],
            as_dict=True,
            )
        self.whdee_name = whdee.w_name
        self.whdee_prefix = whdee.prefix
        # get whdee branch
        whdee_branch = get_branch_address(
            branch=self.whdee_branch
            )
        self.whdee_branch_no = whdee_branch.branch
        self.whdee_branch_addr = whdee_branch.address
