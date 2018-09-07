# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
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
    ]
