// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Wht Cert', {
    refresh: function(frm) {
    },
    whder: function(frm) {
        // get whder branch selection list
        frappe.call({
            method: 'thai_wht.thai_wht.doctype.wht_branch.wht_branch.get_branch_select',
            args: {
                'link_doctype': 'Whder',
                'link_name': frm.doc.whder,
            },
            callback: function(data) {
                $.each(data.message, function(i, item) {
                    $('select[data-fieldname="whder_branch"]')
                    .append($('<option>', {
                        value: item.name,
                        text: item.branch,
                    }));
                });
            },
        });
    },
    whdee: function(frm) {
        // get whdee branch selection list
        frappe.call({
            method: 'thai_wht.thai_wht.doctype.wht_branch.wht_branch.get_branch_select',
            args: {
                'link_doctype': 'Whdee',
                'link_name': frm.doc.whdee,
            },
            callback: function(data) {
                $.each(data.message, function(i, item) {
                    $('select[data-fieldname="whdee_branch"]')
                    .append($('<option>', {
                        value: item.name,
                        text: item.branch,
                    }));
                });
            },
        });
    },
});
