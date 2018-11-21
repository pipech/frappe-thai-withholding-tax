# -*- coding: utf-8 -*- 

from thai_wht.setup.install import make_fixture_records


def execute():
    record = [
        ## Thai Wht
        ### General
        {'doctype': 'Translation', 'language': 'en',
            'source_name': 'Tax Id', 'target_name': u'เลขประจำตัวผู้เสียภาษีอากร'},
    ]
    make_fixture_records(record)
