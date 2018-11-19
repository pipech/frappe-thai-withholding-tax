# -*- coding: utf-8 -*- 

from thai_wht.setup.install import make_fixture_records


def execute():
    record = [
        ## Thai Wht
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Wht Cert Summary', 'target_name': u'ตารางรายการหนังสือรับรองการหักภาษี ณ ที่จ่าย'},
        ### General
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Doc No', 'target_name': u'เลขที่'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Pnd Type', 'target_name': u'ภ.ง.ด.'},
        ### Report
        #### Wht Cert Summary
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Short Pnd', 'target_name': u'เอกสารภ.ง.ด.'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Wht Paid', 'target_name': u'เงินที่จ่าย'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Wht Wht', 'target_name': u'ภาษีที่หัก'},
        ## Frappe
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Standard Reports', 'target_name': u'รายงานทั่วไป'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Setup', 'target_name': u'ตั้งค่า'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Documents', 'target_name': u'เอกสาร'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Date', 'target_name': u'วันที่'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Branch', 'target_name': u'สาขาที่'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Prefix', 'target_name': u'คำนำหน้า'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Name', 'target_name': u'ชื่อ'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Month', 'target_name': u'เดือน'},
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Year', 'target_name': u'ปี'},
    ]
    make_fixture_records(record)
