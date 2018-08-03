// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whder', {
    refresh: function(frm) {
        // format tax_id input
        if (frm.doc.__islocal) {
            frm.cleave = {};
            frm.cleave.tax_id = new Cleave(
                $('[data-fieldname="tax_id"] input').last(),
                {
                    numericOnly: true,
                    blocks: [1, 4, 5, 2, 1],
                }
            );
        }

        // branch list
        frappe.dynamic_link = {
            doc: frm.doc, fieldname: 'name', doctype: 'Whder',
        };

        frm.toggle_display(['address_html'], !frm.doc.__islocal);

        if (frm.doc.__islocal) {
            branchList.clear(frm);
        } else {
            branchList.render(frm);
        }
    },
});
