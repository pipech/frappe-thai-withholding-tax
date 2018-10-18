# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _

from thai_wht.thai_wht.doctype.setup_progress.setup_progress import update_state
from thai_wht.thai_wht.doctype.setup_progress.setup_progress import get_state


@frappe.whitelist()
def update_default_domain_actions_and_get_state():
    update_state()
    return get_state()
