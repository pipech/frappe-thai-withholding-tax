# -*- coding: utf-8 -*- 

import frappe
import os
import functools
import json

from frappe.utils import cint
from os import listdir


@frappe.whitelist()
def check_password(pwd):
    from frappe.utils.password import check_password
    user = frappe.session.user
    try:
        return check_password(user, pwd)
    except frappe.AuthenticationError:
        return 'wrong password'


@frappe.whitelist()
def delete_transaction():
    frappe.only_for('System Manager')
    if frappe.conf.demo:
        # get all doctype in thai_wht app
        thai_wht_doc_path = frappe.get_app_path(
            'thai_wht',
            'thai_wht',
            'doctype'
            )
        thai_wht_doc = listdir(thai_wht_doc_path)

        # loop through all doctype
        for doctype in thai_wht_doc:
            # get doctype name
            if os.path.isdir(os.path.join(thai_wht_doc_path, doctype)):
                doc_json = os.path.join(
                    thai_wht_doc_path,
                    doctype,
                    '{doctype}.json'.format(doctype=doctype)
                    )
                with open(doc_json) as doc_json_value:
                    json_data = json.load(doc_json_value)
                    doctype_name = json_data['name']

                    # delete doctype
                    delete_for_doctype(doctype_name)

        # after deletion
        adding_pre_config_value()
        disable_delete()


def delete_for_doctype(doctype):
    # delete parent
    frappe.db.sql(
        """
        DELETE FROM
            `tab{doctype}`
        ;""".format(doctype=doctype),
        auto_commit=1
        )

    # delete version log
    frappe.db.sql(
        """
        DELETE FROM
            `tabVersion`
        WHERE
            `docname`='{doctype}'
        ;""".format(doctype=doctype),
        auto_commit=1
        )

    # delete series
    frappe.db.sql(
        """
        DELETE FROM
            `tabSeries`
        WHERE
            `name` LIKE 'WHT%'
        ;""",
        auto_commit=1
        )


def disable_delete():
    from frappe.utils import cstr
    site_name = cstr(frappe.local.site)

    # delete data from tabDesktop Icon
    frappe.db.sql(
        """
        DELETE FROM
            `tabDesktop Icon`
        WHERE
            `module_name`='Demo Delete'
        ;""",
        auto_commit=1
        )
    # set site config
    call_bench([
        'bench',
        '--site', site_name,
        'set-config',
        'demo',
        '0'
        ])
    # bench site clear cache
    call_bench([
        'bench',
        '--site', site_name,
        'clear-cache'
        ])


def call_bench(cmd):
    import subprocess
    from subprocess import check_output
    try:
        check_output(
            cmd,
            cwd='/home/frappe/bench',
            stderr=subprocess.STDOUT,
            )
    except subprocess.CalledProcessError as err:
        raise Exception(err.output)


def adding_pre_config_value():
    from thai_wht.setup.install import add_fixture
    add_fixture(only=['wht_records'])
