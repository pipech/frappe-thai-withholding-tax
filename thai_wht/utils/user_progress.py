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
            action_name='Add Wht Cert',
            title='เพิ่มหนังสือรับรองการหักภาษี ณ ที่จ่าย',
            help='สวัสดี สวัสดีนายครับ เย่เย้ ไม่อยากเป็นแปรงสีฟันที่รอวันจะทิ้งลงตระกร้า ไม่ใช่ว่าใจฉันด้านชาเจ็บปวดขึ้นมาใครจะดูและ',
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
            action_name='Add Pnd',
            title='เพิ่มแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.',
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
        # frappe._dict(
        #     action_name='Add Whder',
        #     title='เพิ่มผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
        #     help=_("Example: Basic Mathematics"),
        #     fields=[],
        #     add_more=1, max_count=3, mandatory_entry=1,
        #     submit_method="erpnext.utilities.user_progress_utils.create_course",
        #     done_state_title=_("Go to Courses"),
        #     done_state_title_route=["List", "Course"],
        #     help_links=[
        #         {
        #             "label": _('Add Students'),
        #             "route": ["List", "Student"]
        #         }
        #     ]
        # ),
        # frappe._dict(
        #     action_name='Add Whdee',
        #     title='เพิ่มผู้ถูกหักภาษี ณ ที่จ่าย',
        #     help=_("Example: Basic Mathematics"),
        #     fields=[],
        #     add_more=1, max_count=3, mandatory_entry=1,
        #     submit_method="erpnext.utilities.user_progress_utils.create_course",
        #     done_state_title=_("Go to Courses"),
        #     done_state_title_route=["List", "Course"],
        #     help_links=[
        #         {
        #             "label": _('Add Students'),
        #             "route": ["List", "Student"]
        #         }
        #     ]
        # ),
    ]

    for s in progress_slides:
        s.mark_as_done_method = 'thai_wht.thai_wht.doctype.setup_progress.setup_progress.set_action_completed_state'
        s.done = get_action_completed_state(s.action_name) or 0
        slides.append(s)

    return slides
