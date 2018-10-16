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
            title='หนังสือรับรองการหักภาษี ณ ที่จ่าย',
            help="""
            <p>คุณสามารถออก หนังสือรับรองการหักภาษี ณ ที่จ่าย ได้โดยง่าย เพียงแค่กรอกข้อมูล</p>
            <ul>
                <li>แบบภ.ง.ด.</li>
                <li>ผู้ถูกหักภาษี ณ ที่จ่าย</li>
                <li>ผู้มีหน้าที่หักภาษี ณ ที่จ่าย</li>
                <li>ประเภทเงินได้ จำนวนเงินที่จ่าย และอัตราภาษีที่หัก</li>
            </ul>
            <p>
                โปรแกรมจะช่วยกรอกข้อมูลอื่นๆ เช่น ที่อยู่ของ ผู้ถูกหักภาษี ณ ที่จ่าย,
                ที่อยู่ของ ผู้มีหน้าที่หักภาษี ณ ที่จ่าย, เลขที่หนังสือรับรองการหักภาษี ณ ที่จ่าย
            </p>
            <hr>
            <p class="lead">เลขที่หนังสือรับรองการหักภาษี ณ ที่จ่าย</p>
            <p>
                เลขที่หนังสือรับรองการหักภาษี ณ ที่จ่ายจะอยู่ในรูปแบบ
                <b>WHT X YY MM ####</b> โดยแต่ละหลักจะมีความหมายดังนี้
            </p>
            <ul>
                <li>X ลำดับที่ ของ ผู้มีหน้าที่หักภาษี ณ ที่จ่าย [0-9]</li>
                <li>YY เลขท้าย 2 ตัว ของปีที่ออกหนังสือรับรอง</li>
                <li>MM เดือนที่ออกหนังสือรับรอง</li>
                <li>#### ลำดับที่ของหนังสือรับรอง เริ่มรันใหม่ทุกเดือน</li>
            </ul>
            <p>
                เช่น WHT018120001 หมายถึง หนังสือรับรองการหักภาษี ณ ที่จ่าย <br>
                ลำดับที่ 1 ของเดือน 12 ปี 2018 ของบริษัทลำดับที่ 0
            </p>
            <hr>
            <p class="lead">สถานะของเอกสารหนังสือรับรองการหักภาษี ณ ที่จ่าย</p>
            <img src="https://lh6.googleusercontent.com/lmwA_A3w9ilu_QhxL0e1tAqMZnRoyVFEUV-CZqTJYxEhL77tNupxvre67_V6_tvo9jSGpgx9k1TTSTl2z18lC-pRkCQXKhyPpK2b-Z_aSvbd_17mgB3LFoFG8mP62nSezzzKGM2l" class="img-responsive">
            <br>
            <ul>
                <li>
                    <b>Draft</b>
                     - เอกสารร่าง สามารถแก้ไข หรือลบเอกสารทิ้งได้
                </li>
                <li>
                    <b>Confirmed</b>
                     - เอกสารยืนยันแล้ว ไม่สามารถแก้ไขได้
                    หรือลบเอกสารทิ้งได้ แต่สามารถยกเลิกได้
                </li>
                <li>
                    <b>Submitted</b>
                     - เอกสารที่นำไปยื่น ภ.ง.ด. แล้ว ไม่สามารถแก้ไขหรือลบทิ้งได้
                </li>
                <li>
                    <b>Canceled</b>
                     - เอกสารที่ถูกยกเลิก ไม่สามารถแก้ไข หรือลบเอกสารทิ้งได้
                </li>
            </ul>
            <p>
                การออกแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด. แบบอัตโนมัติ
                โปรแกรมจะดึงข้อมูลจากหนังสือรับรองการหักภาษี ณ ที่จ่าย ที่มีสถานะ Confirmed เท่านั้น
            </p>
            """,
            done_state_title='เพิ่มหนังสือรับรองการหักภาษี ณ ที่จ่าย เรียบร้อย',
            done_state_title_route=['List', 'Wht Cert'],
            fields=[],
        ),
        frappe._dict(
            action_name='addPnd',
            title='แบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.',
            help="""
            <p>
                คุณสามารถออก แบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.
                ได้โดยไม่ต้องกรอกข้อมูลซ้ำซ้อน
            </p>
            <p>
                <b>
                    โปรแกรมจะทำการดึงข้อมูลจาก หนังสือรับรองการหักภาษี ณ ที่จ่าย
                    ที่มีสถานะ Confirmed
                </b>
                เพื่อสร้าง แบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด. โดยอัตโนมัติ
            </p>
            <hr>
            <p class="lead">สถานะของเอกสารแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.</p>
            <img src="https://lh4.googleusercontent.com/BBjJLMTgrJ915jihiR1dUNFC35G0YiHbR3HWgMTHcv6rn6_mjjFRkIcowBuM4kSEBQXHJkozsw1mxNN6JfATAcBkOPiUT6fS89o5PdYeYtYCJfECLOs4DG6S0LNpCFNhvObkV8DN" class="img-responsive">
            <br>
            <ul>
                <li>
                    <b>Draft</b>
                     - เอกสารร่าง สามารถแก้ไข หรือลบเอกสารทิ้งได้
                </li>
                <li>
                    <b>Submitted</b>
                     - เอกสารยืนยันแล้ว ไม่สามารถแก้ไขหรือลบทิ้งได้
                </li>
            </ul>
            """,
            done_state_title='เพิ่มแบบยื่นรายการภาษีเงินได้หัก ณ ที่จ่าย ภ.ง.ด.',
            done_state_title_route=['List', 'Pnd'],
            fields=[],
        ),
        frappe._dict(
            action_name='addWhder',
            title='ผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
            help="""
            <p>
                <b>คุณสามารถเพิ่มผู้มีหน้าที่หักภาษี ณ ที่จ่าย ได้สูงสุด 10 บริษัท โดยไม่จำกัดจำนวนสาขา</b>
            </p>
            <ul>
                <li>
                    บริษัทที่เพิ่มในบัญชีเดียวกัน ควรเป็นบริษัทที่เกี่ยวเนื่องกัน เช่น บริษัทในเครือ หรือบริษัทลูก
                    ที่แชร์พนักงานร่วมกัน หรือแชร์ผู้ถูกหักภาษี ณ ที่จ่ายร่วมกัน
                </li>
                <li>
                    หากเป็นบริษัทที่ไม่เกี่ยวข้องกัน คุณสามารถสร้างบัญชีใหม่ได้ที่
                    <a href="https://pnd.in.th" target="_blank">https://pnd.in.th</a>
                </li>
            </ul>
            """,
            done_state_title='เพิ่มผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
            done_state_title_route=['List', 'Whder'],
            fields=[],
        ),
        frappe._dict(
            action_name='addWhdee',
            title='ผู้ถูกหักภาษี ณ ที่จ่าย',
            help="""
            <p>
                <b>คุณสามารถเพิ่มผู้ถูกหักภาษี ณ ที่จ่าย ได้อย่างไม่จำกัด</b>
            </p>
            <ul>
                <li>
                    ผู้ถูกหักภาษี ณ ที่จ่ายหนึ่งราย สามารถมี สาขาได้ไม่จำกัด<br>
                </li>
                <li>
                    สาขาหนึ่งสาขา ก็สามารถ มี ผู้ถูกหักภาษี ณ ที่จ่าย ได้ไม่จำกัดเช่นกัน<br>
                    เช่น กรณีที่อยู่ของคนงานต่างด้าว
                </li>
            </ul>
            """,
            done_state_title='เพิ่มผู้ถูกหักภาษี ณ ที่จ่าย',
            done_state_title_route=['List', 'Whdee'],
            fields=[],
        ),
        frappe._dict(
            action_name='deleteDemo',
            title='ลบข้อมูลตัวอย่าง',
            help="""
            <p>
                เมื่อคุณพร้อมแล้ว คุณสามารถลบข้อมูลตัวอย่าง และเริ่มต้นใช้งานได้เลย<br>
                <b>เพียงกรอกพาสเวิร์ด และกด submit ด้านล่าง</b>
            </p>
            """,
            fields=[
                {
                    'fieldtype': 'Password',
                    'fieldname': 'pwd',
                    'label': 'พาสเวิร์ด',
                }
            ],
            submit_method='erpnext.utilities.user_progress_utils.create_course',
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
