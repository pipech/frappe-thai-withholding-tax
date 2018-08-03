// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Wht Cert', {
    refresh: function(frm) {
        setDefaultDate(frm);
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
        // filter whdee field by pnd
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
    wht_cert_detail_on_form_rendered: function(frm) {
        // hide add row button if wht child table have 3 entry
        let hideBool = (frm.doc.wht_cert_detail.length < 3);
        $('[data-fieldname="wht_cert_detail"] button.grid-add-row').toggle(hideBool);
        $('[data-fieldname="wht_cert_detail"] button.grid-insert-row-below').toggle(hideBool);
        $('[data-fieldname="wht_cert_detail"] button.grid-insert-row').toggle(hideBool);

        setChildTblDefaultValue(frm.open_grid_row(), frm.doc.date);
    },
});

/**
 * set default date for date field
 * @param {object} frm - form object from frappe
 */
function setDefaultDate(frm) {
    let today = frappe.datetime.nowdate();
    frm.set_value('date', today);
}

/**
 * set default date for date field on child table
 * @param {object} gridRow - form object from frappe
 * @param {date} date - date from date field
 */
function setChildTblDefaultValue(gridRow, date) {
    if (typeof date === 'undefined') {
        date = frappe.datetime.nowdate();
    }
    if (typeof gridRow.doc.date === 'undefined') {
        frappe.model.set_value(
            gridRow.doc.doctype,
            gridRow.doc.name,
            'date',
            date
        );
    }
    frappe.model.set_value(
        gridRow.doc.doctype,
        gridRow.doc.name,
        'condition',
        1
    );
}
