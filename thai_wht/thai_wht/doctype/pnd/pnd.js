// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pnd', {
    whder: function(frm) {
        branchList.branchSelectionQuery(
            'Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch'
        );
    },
    refresh: (frm) => {
        branchList.branchSelectionQuery(
            'Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch'
        );

        if (frm.doc.docstatus !== 0 && frm.doc.__islocal !== 1) {
            frm.add_custom_button(__('Print'), async function() {
                let w = window.open(
                    frappe.urllib.get_full_url(
                        '/api/method/thai_wht.thai_wht.report.pnd_attach.pnd_attach.download_pdf_pnd?'
                        + 'name=' + encodeURIComponent(me.frm.doc.name)
                    )
                );
                if (!w) {
                    frappe.msgprint(__('Please enable pop-ups')); return;
                }
            });
        }
    },
});
