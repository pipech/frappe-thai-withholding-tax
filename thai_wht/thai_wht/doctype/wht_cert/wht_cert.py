# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import datetime
import frappe

from frappe.model.document import Document
from thai_wht.thai_wht.doctype.wht_branch.wht_branch import get_branch_address


class WhtCert(Document):
    def autoname(self):
        from frappe.model.naming import make_autoname
        whder = frappe.get_value(
            doctype='Whder',
            filters=self.whder,
            fieldname=['whder_no'],
            as_dict=True,
            )
        self.whder_no = whder.whder_no
        self.name = make_autoname(
            'WHT{whder_no}.YY.{cert_month}.####'.format(
                whder_no=self.whder_no,
                cert_month=self.date[5:7]
                )
            )

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

    def validate(self):
        err_msg = []
        try:
            cert_month = self.date.month
        except AttributeError:
            cert_month = datetime.datetime.strptime(self.date, '%Y-%m-%d').month
        for d in self.wht_cert_detail:
            try:
                cert_detail_month = d.date.month
            except AttributeError:
                cert_detail_month = datetime.datetime.strptime(d.date, '%Y-%m-%d').month
            if cert_detail_month != cert_month:
                err_msg.append(
                    'วันที่จ่ายเงินของรายการที่ {idx} ยอดเงิน {paid} ไม่ตรงกับเดือนที่ออกหนังสือรับรอง'.format(
                        idx=d.idx,
                        paid='{:,.2f}'.format(d.paid),
                        )
                    )
        if err_msg:
            err_msg = '<br>'.join(err_msg)
            frappe.throw(err_msg, 'ไม่สามารถบันทึกรายการได้')
