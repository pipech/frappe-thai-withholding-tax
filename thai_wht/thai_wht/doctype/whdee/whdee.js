// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whdee', {
    refresh: function(frm) {
        if (frm.doc.docstatus !== 1) {
            frm.cleave = {};
            frm.cleave.tax_id = new Cleave(
                $('[data-fieldname="tax_id"] input').last(),
                {
                    numericOnly: true,
                    blocks: [1, 4, 5, 2, 1],
                }
            );
        }

        // frappe.dynamic_link = {
        //     doc: frm.doc, fieldname: 'name', doctype: 'Whdee',
        // };

        frm.toggle_display(['address_html'], !frm.doc.__islocal);

        if (frm.doc.__islocal) {
            frappe.contacts.clear_address_and_contact(frm);
        } else {
            frappe.contacts.render_address_and_contact(frm);
        }
    },
});
