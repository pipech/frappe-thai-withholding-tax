# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Pnd(Document):
    pass


@frappe.whitelist()
def autogen():
    print('asdasdsadsa')
    print('asdasdsadsa')
    print('asdasdsadsa')
    print('asdasdsadsa')
    return 'aaa'
