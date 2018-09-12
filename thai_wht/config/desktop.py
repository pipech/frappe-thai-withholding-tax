# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

import frappe


def get_data():
    icons = [
        {
            'module_name': 'Thai Wht',
            'color': 'green',
            'icon': 'octicon octicon-repo-force-push',
            'type': 'module',
            'label': _('Thai Wht')
        },
        {
            'module_name': 'Wht Cert',
            'color': 'green',
            'icon': 'octicon octicon-file-code',
            'type': 'link',
            '_doctype': 'Wht Cert',
            'link': 'List/Wht Cert',
            'label': _('Wht Cert')
        },
        {
            'module_name': 'Wht Manual',
            'color': '#589494',
            'icon': 'octicon octicon-book',
            'type': 'page',
            'link': 'wht-manual',
            'label': _('Wht Manual')
        },
    ]
    if frappe.conf.demo == 1:
        icons.append({
            'module_name': 'Demo Delete',
            'color': '#ffa00a',
            'icon': 'octicon octicon-trashcan',
            'type': 'page',
            'link': 'delete_transaction',
            'label': _('Demo Delete')
        })
    return icons
