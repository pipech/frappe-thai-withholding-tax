# -*- coding: utf-8 -*- 

import frappe
import os
import functools
import json

from frappe.utils import cstr
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
def delete_demo(pwd):
    # check password
    if check_password(pwd) == 'wrong password':
        return {
            'status': 'fail',
            'fail': 'Wrong password',
            }

    # check site config
    if frappe.conf.demo == '2':
        delete_transaction()
        return {
            'status': 'fail',
            'fail': 'There are already running process or uncaught error',
            }
    elif frappe.conf.demo != '1':
        return {
            'status': 'fail',
            'fail': 'There are no demo',
            }

    # check roles
    frappe.only_for('System Manager')

    # get site name
    site_name = cstr(frappe.local.site)

    # start process
    stages = [
        {
            'status': 'Starting process',
            'fail_msg': 'Failed : Starting process',
            'tasks': [
                {
                    'fn': set_site_demo_config,
                    'args': {
                        'site_name': site_name,
                        'demo_config': '2',
                    },
                    'fail_msg': 'Failed : Set site demo config to 2'
                },
            ]
        },
        {
            'status': 'Delete demo transaction',
            'fail_msg': 'Failed : Delete demo transaction',
            'tasks': [
                {
                    'fn': delete_transaction,
                    'args': '',
                    'fail_msg': 'Failed : Delete demo transaction'
                },
            ]
        },
        {
            'status': 'Adding pro config value',
            'fail_msg': 'Failed : Adding pro config value',
            'tasks': [
                {
                    'fn': adding_pre_config_value,
                    'args': '',
                    'fail_msg': 'Failed : Adding pro config value'
                },
            ]
        },
        {
            'status': 'Finishing up',
            'fail_msg': 'Failed : Finishing up',
            'tasks': [
                {
                    'fn': delete_desktop_icon,
                    'args': '',
                    'fail_msg': 'Failed : Delete desktop icon'
                },
                {
                    'fn': clear_cache,
                    'args': site_name,
                    'fail_msg': 'Failed : Clear cache'
                },
                {
                    'fn': set_site_demo_config,
                    'args': {
                        'site_name': site_name,
                        'demo_config': '0',
                    },
                    'fail_msg': 'Failed : Set site demo config to 0'
                },
            ]
        },
    ]
    try:
        current_task = {}
        for idx, stage in enumerate(stages):
            frappe.publish_realtime(
                'delete_demo',
                {
                    'progress': [idx, len(stages)],
                    'stage_status': stage.get('status'),
                },
                user=frappe.session.user
                )
            for task in stage.get('tasks'):
                current_task = task
                task.get('fn')(task.get('args'))
    except Exception as err:
        print(err)
        return {
            'status': 'fail',
            'fail': current_task.get('fail_msg'),
            'err_str': err,
            }
    else:
        return {'status': 'ok'}


def delete_transaction(args):
    frappe.only_for('System Manager')

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


def delete_for_doctype(doctype):
    frappe.db.sql(
        'DELETE FROM `tab{doctype}`;'.format(doctype=doctype)
        )
    frappe.db.sql(
        """
        DELETE FROM `tabVersion` WHERE `docname`='{doctype}';
        """.format(doctype=doctype)
        )
    frappe.db.sql(
        'DELETE FROM `tabSeries` WHERE `name` LIKE "WHT%";'
        )
    frappe.db.commit()


def set_site_demo_config(args):
    demo_config = args.get('demo_config')
    site_name = args.get('site_name')
    # set site config
    call_bench([
        'bench',
        '--site', site_name,
        'set-config',
        'demo',
        demo_config
        ])


def delete_desktop_icon(args):
    frappe.db.sql(
        """
        DELETE FROM
            `tabDesktop Icon`
        WHERE
            `module_name`='Demo Delete'
        ;""",
        auto_commit=1
        )


def clear_cache(site_name):
    # bench site clear cache
    call_bench([
        'bench',
        '--site', site_name,
        'clear-cache'
        ])


def adding_pre_config_value(args):
    from thai_wht.setup.install import add_fixture
    add_fixture(only=['wht_records'])


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
