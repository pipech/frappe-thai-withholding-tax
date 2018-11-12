# -*- coding: utf-8 -*- 

import frappe
import os
import functools
import json

from frappe.utils import cstr
from frappe.utils import cint
from thai_wht.setup.install import add_fixture
from thai_wht.setup.install import make_fixture_records
from thai_wht.thai_wht.doctype.wht_branch.wht_branch import get_branch_select
from thai_wht.thai_wht.doctype.pnd.pnd import autogen
from os import listdir


def add_demo():
    if frappe.conf.demo == 1:
        add_whder_whdee()
        add_wht_cert()
        add_payer()
        autogen()


def add_wht_cert():
    demo_wht_cert = [
        {
            'doctype': 'Wht Cert',
            'workflow_state': 'Confirmed',
            'pnd': '3',
            'date': '2018-09-01',
            'whder': '1111111111119',
            'whdee': '1472174703381',
            'wht_cert_detail': [
                {
                    'date': '2018-09-01',
                    'type': u'8 อื่นๆ - ค่าบริการ',
                    'type_detail': u'รักษาความสงบของบ้านเมือง',
                    'paid': 100000,
                    'rate': 3,
                    'wht': 3000,
                    'condition': '1',
                }
            ],
        },
        {
            'doctype': 'Wht Cert',
            'workflow_state': 'Confirmed',
            'pnd': '3',
            'date': '2018-09-02',
            'whder': '2222222222227',
            'whdee': '8432740761025',
            'wht_cert_detail': [
                {
                    'date': '2018-09-02',
                    'type': u'8 อื่นๆ - รางวัลในการประกวด แข่งขัน ชิงโชค',
                    'paid': 200000,
                    'rate': 3,
                    'wht': 6000,
                    'condition': '1',
                }
            ],
        },
        {
            'doctype': 'Wht Cert',
            'workflow_state': 'Confirmed',
            'pnd': '3',
            'date': '2018-09-03',
            'whder': '1111111111119',
            'whdee': '8432740761025',
            'wht_cert_detail': [
                {
                    'date': '2018-09-03',
                    'type': u'8 อื่นๆ - ค่าบริการ',
                    'paid': 1000,
                    'rate': 3,
                    'wht': 30,
                    'condition': '1',
                },
                {
                    'date': '2018-09-03',
                    'type': u'5 ค่าเช่า',
                    'paid': 20000,
                    'rate': 5,
                    'wht': 1000,
                    'condition': '1',
                }
            ],
        },
        {
            'doctype': 'Wht Cert',
            'workflow_state': 'Confirmed',
            'pnd': '53',
            'date': '2018-09-07',
            'whder': '2222222222227',
            'whdee': '4631360706604',
            'wht_cert_detail': [
                {
                    'date': '2018-09-07',
                    'type': u'8 อื่นๆ - ค่าจ้างทำของ',
                    'paid': 35000,
                    'rate': 3,
                    'wht': 1050,
                    'condition': '1',
                }
            ],
        },
        {
            'doctype': 'Wht Cert',
            'workflow_state': 'Confirmed',
            'pnd': '53',
            'date': '2018-09-10',
            'whder': '2222222222227',
            'whdee': '4631360706604',
            'wht_cert_detail': [
                {
                    'date': '2018-09-10',
                    'type': u'8 อื่นๆ - ค่าจ้างทำของ',
                    'paid': 25000,
                    'rate': 3,
                    'wht': 750,
                    'condition': '1',
                }
            ],
        },
        {
            'doctype': 'Wht Cert',
            'workflow_state': 'Confirmed',
            'pnd': '53',
            'date': '2018-09-13',
            'whder': '1111111111119',
            'whdee': '1625011011065',
            'wht_cert_detail': [
                {
                    'date': '2018-09-13',
                    'type': u'7 การรับเหมาที่ผู้รับเหมาต้องลงทุนด้วยการจัดหาสัมภาระ',
                    'paid': 56000,
                    'rate': 3,
                    'wht': 1680,
                    'condition': '1',
                }
            ],
        },
    ]

    # add branch name
    for wht_cert in demo_wht_cert:
        whder_branch = get_branch_select('Whder', wht_cert['whder'])[0]['name']
        whdee_branch = get_branch_select('Whdee', wht_cert['whdee'])[0]['name']
        wht_cert['whder_branch'] = whder_branch
        wht_cert['whdee_branch'] = whdee_branch

    # add record
    make_fixture_records(demo_wht_cert)


def add_whder_whdee():
    demo_records = [
        # Whder
        {
            'doctype': 'Whder',
            'tax_id': '1 1111 11111 11 9',
            'prefix': u'บจก.',
            'w_name': u'สตาร์ค อินดัสตรี้',
        },
        {
            'doctype': 'Whder',
            'tax_id': '2 2222 22222 22 7',
            'prefix': u'บจก.',
            'w_name': u'ทาร์แกเรียน',
        },
        # Whdee
        {
            'doctype': 'Whdee',
            'tax_id': '1 4721 74703 38 1',
            'prefix': u'นาย',
            'w_name': u'จอห์น สโนว์',
        },
        {
            'doctype': 'Whdee',
            'tax_id': '8 4327 40761 02 5',
            'prefix': u'นาย',
            'w_name': u'มิยาโมโตะ มุซาชิ',
        },
        {
            'doctype': 'Whdee',
            'tax_id': '4 6313 60706 60 4',
            'prefix': u'หจก.',
            'w_name': u'แพลนเนท เอ็กเพรส',
        },
        {
            'doctype': 'Whdee',
            'tax_id': '1 6250 11011 06 5',
            'prefix': u'บมจ.',
            'w_name': u'ดันเดอร์ มิฟฟลิน',
        },
        # Wht Branch
        {
            'doctype': 'Wht Branch',
            'branch': '00000',
            'address_line1': u'11',
            'moo_ban': u'ไอรอนแมน',
            'sub_district': u'เหล',
            'district': u'กะปง',
            'province': u'พังงา',
            'zip_code': u'12345',
            'links': [
                {
                    'link_doctype': 'Whder',
                    'link_name': '1111111111119',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00001',
            'address_line1': u'12',
            'moo_ban': u'โกลด์แมน',
            'sub_district': u'แมด',
            'district': u'ลืออำนาจ',
            'province': u'อำนาจเจริญ',
            'links': [
                {
                    'link_doctype': 'Whder',
                    'link_name': '1111111111119',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00000',
            'address_line1': u'22',
            'soi': u'ทาแก 27',
            'sub_district': u'ทากาศ',
            'district': u'แม่ทา',
            'province': u'ลำพูน',
            'links': [
                {
                    'link_doctype': 'Whder',
                    'link_name': '2222222222227',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00000',
            'address_line1': '32',
            'sub_district': u'สันกำแพง',
            'district': u'สันกำแพง',
            'province': u'เชียงใหม่',
            'zip_code': u'10123',
            'links': [
                {
                    'link_doctype': 'Whdee',
                    'link_name': '1472174703381',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00000',
            'address_line1': '1',
            'sub_district': u'ปุโละปุโย',
            'district': u'หนองจิก',
            'province': u'ปัตตานี',
            'links': [
                {
                    'link_doctype': 'Whdee',
                    'link_name': '8432740761025',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00000',
            'address_line1': u'3973',
            'road': u'ดาวเหนือ',
            'sub_district': u'ดาวเรือง',
            'district': u'เมืองสระบุรี',
            'province': u'สระบุรี',
            'links': [
                {
                    'link_doctype': 'Whdee',
                    'link_name': '4631360706604',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00322',
            'address_line1': u'44223',
            'sub_district': u'ดาวคะนอง',
            'district': u'ธนบุรี',
            'province': u'กรุงเทพมหานคร',
            'zip_code': u'10160',
            'links': [
                {
                    'link_doctype': 'Whdee',
                    'link_name': '4631360706604',
                }
            ],
        },
        {
            'doctype': 'Wht Branch',
            'branch': '00008',
            'address_line1': u'82',
            'sub_district': u'ดงกระทงยาม',
            'district': u'ศรีมหาโพธิ',
            'province': u'ปราจีนบุรี',
            'links': [
                {
                    'link_doctype': 'Whdee',
                    'link_name': '1625011011065',
                }
            ],
        },
    ]
    make_fixture_records(demo_records)


def add_payer():
    demo_records = [
        # Payer
        {
            'doctype': 'Payer',
            'prefix': u'นาย',
            'p_name': u'สมประสงค์ ดีใจ',
            'position': u'ผู้จัดการบัญชี',
        },
    ]
    make_fixture_records(demo_records)


def commit_pnd():
    pnd_list = frappe.get_all(
        doctype='Pnd',
    )
    for pnd in pnd_list:
        pnd_doc = frappe.get_doc('Pnd', pnd['name'])
        pnd_doc.submit()


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
        return {
            'status': 'fail',
            'fail': 'There are already running process or uncaught error',
            }
    elif frappe.conf.demo != 1:
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
            'status': 'Adding pre config value',
            'fail_msg': 'Failed : Adding pre config value',
            'tasks': [
                {
                    'fn': adding_pre_config_value,
                    'args': '',
                    'fail_msg': 'Failed : Adding pre config value'
                },
            ]
        },
        {
            'status': 'Clear setup progress',
            'fail_msg': 'Failed : Clear setup progress',
            'tasks': [
                {
                    'fn': clear_completed_state,
                    'args': '',
                    'fail_msg': 'Failed : Clear setup progress'
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
                {
                    'fn': update_site_status_delete_demo,
                    'args': {
                        'site_name': site_name,
                    },
                    'fail_msg': 'Failed : Update site status to 3'
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
    dont_delete_doctype = ['Setup Progress', 'Setup Progress Action']

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

                if doctype_name not in dont_delete_doctype:
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
    add_fixture(only=['wht_records'])


def clear_completed_state(args):
    setup_progress = frappe.get_single('Setup Progress')
    setup_progress.done = 1
    setup_progress.save()


def update_site_status_delete_demo(args):
    pnd_site = 'pnd.in.th'

    full_site_name = args.get('site_name')
    subdomain = full_site_name.split('.')[0]
    kwargs = "{{'domain': '{d}'}}".format(
        d=subdomain
    )
    call_bench([
        'bench',
        '--site', pnd_site,
        'execute',
        '--kwargs', kwargs,
        'pnd_site.utils.site_setup.update_site_status_to_del_demo'
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
