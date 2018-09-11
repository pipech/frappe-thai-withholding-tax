# -*- coding: utf-8 -*- 
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

import frappe

from frappe.desk.doctype.desktop_icon.desktop_icon import set_hidden_list


def after_install():
    add_fixture()
    hidden_icon = [
        'Desk',
        'File Manager',
        'Website', 'Integrations',
        'Setup',
        'Email Inbox',
        'Core',
        'Contacts',
        ]
    set_hidden_list(hidden_icon)
    

def add_fixture(only=''):
    fixture = {
        'wht_records': [
            # Prefix
            {'doctype': 'Prefix', 'prefix': u'นาย', 'type': 'Ind'},
            {'doctype': 'Prefix', 'prefix': u'นาง', 'type': 'Ind'},
            {'doctype': 'Prefix', 'prefix': u'นางสาว', 'type': 'Ind'},
            {'doctype': 'Prefix', 'prefix': u'หสม.', 'type': 'Ind'},

            {'doctype': 'Prefix', 'prefix': u'บจก.', 'type': 'Org'},
            {'doctype': 'Prefix', 'prefix': u'บมจ.', 'type': 'Org'},
            {'doctype': 'Prefix', 'prefix': u'หจก.', 'type': 'Org'},

            # Wht Type
            {'doctype': 'Wht Type',
                'wht_type': u'1 เงินเดือนค่าจ้าง เบี้ยเลี้ยง - กรณีทั่วไป',
                'pnd1': 1, 'pnd2': 0, 'pnd3': 0, 'pnd53': 0, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'1 เงินเดือนค่าจ้าง เบี้ยเลี้ยง - กรณีได้รับอนุมัติให้หัก 3%',
                'pnd1': 1, 'pnd2': 0, 'pnd3': 0, 'pnd53': 0, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'1 เงินเดือนค่าจ้าง เบี้ยเลี้ยง - กรณีนายจ้างจ่ายครั้งเดียวเพราะออกจากงาน',
                'pnd1': 1, 'pnd2': 0, 'pnd3': 0, 'pnd53': 0, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'2 ค่าธรรมเนียม ค่านายหน้า - กรณีผู้รับเป็นผู้อยู่ในประเทศไทย',
                'pnd1': 1, 'pnd2': 0, 'pnd3': 0, 'pnd53': 0, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'2 ค่าธรรมเนียม ค่านายหน้า - กรณีผู้รับมิได้เป็นผู้อยู่ในประเทศไทย',
                'pnd1': 1, 'pnd2': 0, 'pnd3': 0, 'pnd53': 0, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'2 ค่าธรรมเนียม ค่านายหน้า - กรณีนายจ้างจ่ายครั้งเดียวเพราะออกจากงาน',
                'pnd1': 1, 'pnd2': 0, 'pnd3': 0, 'pnd53': 0, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'3 ค่าแห่งลิขสิทธิ์',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ก ดอกเบี้ย',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ข เงินปันผล - ได้รับเครดิตภาษี',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ข เงินปันผล - ไม่ได้รับเครดิตภาษี - กำไรสุทธิของกิจการที่ได้รับยกเว้นภาษีเงินได้นิติบุคคล',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ข เงินปันผล - ไม่ได้รับเครดิตภาษี - เงินปันผลหรือเงินส่วนแบ่งของกำไรที่ได้รับยกเว้น ...',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ข เงินปันผล - ไม่ได้รับเครดิตภาษี - กำไรสุทธิส่วนที่ได้หักผลขาดทุนสุทธิยกมาไม่เกิน 5 ปี ...',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ข เงินปันผล - ไม่ได้รับเครดิตภาษี - กำไรที่รับรู้ทางบัญชีโดยวิธีส่วนได้เสีย',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 ข เงินปันผล - ไม่ได้รับเครดิตภาษี - อื่นๆ',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'4 อื่นๆ',
                'pnd1': 0, 'pnd2': 1, 'pnd3': 0, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'5 ค่าเช่า',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'6 เงินได้จากวิชาชีพอิสระ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 1},
            {'doctype': 'Wht Type',
                'wht_type': u'7 การรับเหมาที่ผู้รับเหมาต้องลงทุนด้วยการจัดหาสัมภาระ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าจ้างทำของ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าบริการ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าโฆษณา',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าขายอสังหาริมทรัพย์',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าแสดงของนักแสดงสาธารณะ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าเบี้ยประกันวินาศภัย',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าขนส่งที่มิใช่ค่าขนส่งสาธารณะ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - ค่าซื้อสินค้าพืชไร่',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - รางวัลในการประกวด แข่งขัน ชิงโชค',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ - รางวัล ส่วนลดหรือประโยชน์ใดๆ จากการส่งเสริมการขาย',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
            {'doctype': 'Wht Type',
                'wht_type': u'8 อื่นๆ',
                'pnd1': 0, 'pnd2': 0, 'pnd3': 1, 'pnd53': 1, 'pnd54': 0},
        ],
        'config_records': [
            # Role
            {'doctype': 'Role', 'role_name': 'Wht Manager', 'desk_access': 1},
            {'doctype': 'Role', 'role_name': 'Wht User', 'desk_access': 1},

            # Workflow State
            {'doctype': 'Workflow State', 'workflow_state_name': 'Draft',
                'style': 'Warning'},
            {'doctype': 'Workflow State', 'workflow_state_name': 'Confirmed',
                'style': 'Success'},
            {'doctype': 'Workflow State', 'workflow_state_name': 'Submitted',
                'style': 'Primary'},
            {'doctype': 'Workflow State', 'workflow_state_name': 'Cancelled',
                'style': 'Danger'},

            # Workflow Action
            {'doctype': 'Workflow Action', 'workflow_action_name': 'Confirm'},
            {'doctype': 'Workflow Action', 'workflow_action_name': 'Submit'},
            {'doctype': 'Workflow Action', 'workflow_action_name': 'Cancel'},

            # Workflow
            {
                'doctype': 'Workflow',
                'workflow_name': 'Wht Cert Workflow',
                'document_type': 'Wht Cert',
                'is_active': 1,
                'states': [
                    {'state': 'Draft', 'doc_status': 0,
                        'allow_edit': 'Wht User'},
                    {'state': 'Confirmed', 'doc_status': 1,
                        'allow_edit': 'Administrator'},
                    {'state': 'Submitted', 'doc_status': 1,
                        'allow_edit': 'Administrator'},
                    {'state': 'Cancelled', 'doc_status': 2,
                        'allow_edit': 'Administrator'},
                ],
                'transitions': [
                    {'state': 'Draft', 'action': 'Confirm',
                        'next_state': 'Confirmed', 'allowed': 'Wht User'},
                    {'state': 'Confirmed', 'action': 'Submit',
                        'next_state': 'Submitted', 'allowed': 'Administrator'},
                    {'state': 'Confirmed', 'action': 'Cancel',
                        'next_state': 'Cancelled', 'allowed': 'Wht Manager'},
                ],
                'workflow_state_field': 'workflow_state',
            },
        ],
        'translation_records': [
            # Translation
            ## Thai Wht
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Thai Wht', 'target_name': u'ภาษีหัก ณ ที่จ่าย'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Wht Manual', 'target_name': u'คู่มือการใช้งาน'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Demo Delete', 'target_name': u'ล้างข้อมูลตัวอย่าง'},
            ### Doctype
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Pnd', 'target_name': u'ภ.ง.ด.'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Wht Cert', 'target_name': u'หนังสือรับรองการหักภาษี ณ ที่จ่าย'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Payer', 'target_name': u'ผู้จ่ายเงิน'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Whdee', 'target_name': u'ผู้ถูกหักภาษี ณ ที่จ่าย'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Whder', 'target_name': u'ผู้มีหน้าที่หักภาษี ณ ที่จ่าย'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Wht Branch', 'target_name': u'สาขา'},
            ## Frappe
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Status', 'target_name': u'สถานะ'},
            {'doctype': 'Translation', 'language': 'en',
                'source_name': 'Add Filter', 'target_name': u'เพิ่มคัดกรอง'},
        ],
    }
    
    records = []
    if only:
        for key in only:
            records.extend(fixture.get(key))
    else:
        for key, value in list(fixture.items()):
            records.extend(value)

    make_fixture_records(records)


def make_fixture_records(records):
    from frappe.modules import scrub
    for r in records:
        doc = frappe.new_doc(r.get('doctype'))
        doc.update(r)

        # ignore mandatory for root
        parent_link_field = ('parent_' + scrub(doc.doctype))
        if doc.meta.get_field(parent_link_field) and not doc.get(parent_link_field):
            doc.flags.ignore_mandatory = True

        try:
            doc.insert(ignore_permissions=True)
        except frappe.DuplicateEntryError as e:
            # pass DuplicateEntryError and continue
            if e.args and e.args[0] == doc.doctype and e.args[1] == doc.name:
                # make sure DuplicateEntryError is for the exact same doc and not a related doc
                pass
            else:
                raise
