// Copyright (c) 2016, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports['Wht Cert Summary'] = {
    'filters': [
        {
            'fieldname': 'whder',
            'label': 'ผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
            'fieldtype': 'Link',
            'options': 'Whder',
        },
    ],
};
