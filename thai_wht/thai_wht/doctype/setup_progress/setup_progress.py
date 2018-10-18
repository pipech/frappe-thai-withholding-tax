# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class SetupProgress(Document):
    pass


def get_setup_progress():
    if not getattr(frappe.local, 'setup_progress', None):
        frappe.local.setup_progress = frappe.get_doc(
            'Setup Progress',
            'Setup Progress'
            )
    return frappe.local.setup_progress


def get_action_completed_state(action_name):
    for d in get_setup_progress().actions:
        if d.action_name == action_name:
            return d.is_completed


def update_action_completed_state(action_name):
    for d in get_setup_progress().actions:
        if d.action_name == action_name:
            update_action(d)


def update_action(doc):
    doctype = doc.action_doctype
    docname = doc.action_document
    field = doc.action_field

    if not doc.is_completed:
        if doc.min_doc_count:
            if frappe.db.count(doctype) >= doc.min_doc_count:
                doc.is_completed = 1
                doc.save()
        if docname and field:
            d = frappe.get_doc(doctype, docname)
            if d.get(field):
                doc.is_completed = 1
                doc.save()


def update_state():
    for d in get_setup_progress().actions:
        update_action(d)


def get_state():
    state = {}
    for d in get_setup_progress().actions:
        state[d.action_name] = d.is_completed
    return state


@frappe.whitelist()
def set_action_completed_state(action_name):
    for d in get_setup_progress().actions:
        if d.action_name == action_name:
            d.is_completed = 1
            d.save()
