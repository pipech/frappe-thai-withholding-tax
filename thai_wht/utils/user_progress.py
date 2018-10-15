# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from thai_wht.thai_wht.doctype.setup_progress.setup_progress import get_action_completed_state


def get_user_progress_slides():
    slides = []
    progress_slides = [
        frappe._dict(
            action_name='addWhtCert',
            title='เพิ่ม หนังสือรับรองการหักภาษี ณ ที่จ่าย',
            help="""
            <h1>สวัสดี</h1>
            <hr>
            <ul>
                <li>ทดสอบ1</li>
                <li>ทดสอบ2</li>
            </ul>
            """,
            fields=[],
            done_state_title='เพิ่มหนังสือรับรองการหักภาษี ณ ที่จ่าย เรียบร้อย',
            done_state_title_route=['List', 'Wht Cert'],
        ),
        frappe._dict(
            action_name='addPnd',
            title='เพิ่ม แบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.',
            help='สวัสดี สวัสดีนายครับ เย่เย้ wwwwwwwwwwww qqqqqqqqqq',
            fields=[],
            submit_method='erpnext.utilities.user_progress_utils.create_course',
            done_state_title='เพิ่มหนังสือรับรองการหักภาษี ณ ที่จ่าย เรียบร้อย',
            done_state_title_route=['List', 'Wht Cert'],
            # help_links=[
            #     {
            #         'label': _('Add Students'),
            #         'route': ['List', 'Student']
            #     }
            # ]
        ),
        frappe._dict(
            action_name='addWhder',
            title='เพิ่ม ผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
            help='สวัสดี สวัสดีนายครับ เย่เย้ wwwwwwwwwwww qqqqqqqqqq',
            fields=[],
            submit_method='erpnext.utilities.user_progress_utils.create_course',
            done_state_title='เพิ่มหนังสือรับรองการหักภาษี ณ ที่จ่าย เรียบร้อย',
            done_state_title_route=['List', 'Wht Cert'],
            # help_links=[
            #     {
            #         'label': _('Add Students'),
            #         'route': ['List', 'Student']
            #     }
            # ]
        ),
        frappe._dict(
            action_name='addWhdee',
            title='เพิ่ม ผู้ถูกหักภาษี ณ ที่จ่าย',
            help="""
            <h1>เพิ่มแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.</h1>
            <ul>
                <li>สวัสดี1</li>
                <li>สวัสดี2</li>
                <li>สวัสดี3</li>
            </ul>
            """,
            fields=[],
            # submit_method='erpnext.utilities.user_progress_utils.create_course',
            done_state_title='เพิ่มแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด. เรียบร้อย',
            done_state_title_route=['List', 'Pnd'],
            # help_links=[
            #     {
            #         'label': _('Add Students'),
            #         'route': ['List', 'Student']
            #     }
            # ]
        ),
        frappe._dict(
            action_name='deleteDemo',
            title='ลบ ข้อมูลตัวอย่าง',
            help="""
            <h1>เพิ่มแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.</h1>
            <ul>
                <li>สวัสดี1</li>
                <li>สวัสดี2</li>
                <li>สวัสดี3</li>
            </ul>
            """,
            fields=[],
            # submit_method='erpnext.utilities.user_progress_utils.create_course',
            done_state_title='เพิ่มแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด. เรียบร้อย',
            done_state_title_route=['List', 'Pnd'],
            # help_links=[
            #     {
            #         'label': _('Add Students'),
            #         'route': ['List', 'Student']
            #     }
            # ]
        ),
    ]

    for s in progress_slides:
        s.mark_as_done_method = 'thai_wht.thai_wht.doctype.setup_progress.setup_progress.set_action_completed_state'
        s.done = get_action_completed_state(s.action_name) or 0
        slides.append(s)

    return slides
