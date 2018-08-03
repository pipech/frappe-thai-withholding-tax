// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Wht Cert', {
    refresh: function(frm) {
    },
    whder: function(frm) {
        // get whder branch selection list
        if (frm.doc.whder) {
            frappe.call({
                method: 'thai_wht.thai_wht.doctype.wht_branch.wht_branch.get_branch_select',
                args: {
                    'link_doctype': 'Whder',
                    'link_name': frm.doc.whder,
                },
                callback: function(data) {
                    let selectField = $('select[data-fieldname="whder_branch"]');
                    selectField.empty();
                    $.each(data.message, function(i, item) {
                        selectField.append($('<option>', {
                            value: item.name,
                            text: item.branch,
                        }));
                    });
                },
            });
        }
    },
    whdee: function(frm) {
        // get whdee branch selection list
        if (frm.doc.whdee) {
            frappe.call({
                method: 'thai_wht.thai_wht.doctype.wht_branch.wht_branch.get_branch_select',
                args: {
                    'link_doctype': 'Whdee',
                    'link_name': frm.doc.whdee,
                },
                callback: function(data) {
                    let selectField = $('select[data-fieldname="whdee_branch"]');
                    selectField.empty();
                    $.each(data.message, function(i, item) {
                        selectField.append($('<option>', {
                            value: item.name,
                            text: item.branch,
                        }));
                    });
                },
            });
        }
    },
    pnd: function(frm) {
        let pnd = frm.doc.pnd;
        let type;
        if (pnd === '1' || pnd === '2' || pnd === '3') {
            type = 'Ind';
        } else {
            type = 'Org';
        }
        frm.set_query('whdee', function() {
            return {
                filters: {
                    type: type,
                },
            };
        });
    },
});
