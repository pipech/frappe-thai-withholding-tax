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

        setupWhtTypeQueries(frm);
    },
    wht_cert_detail_on_form_rendered: function(frm) {
        // hide add row button if wht child table have 3 entry
        let hideBool = (frm.doc.wht_cert_detail.length < 3);
        $('[data-fieldname="wht_cert_detail"] button.grid-add-row').toggle(hideBool);
        $('[data-fieldname="wht_cert_detail"] button.grid-insert-row-below').toggle(hideBool);
        $('[data-fieldname="wht_cert_detail"] button.grid-insert-row').toggle(hideBool);

        setChildTblDefaultValue(frm.open_grid_row(), frm.doc.date);
        setupWhtTypeQueries(frm);
    },
});

frappe.ui.form.on('Wht Cert Detail', {
    // event triggred when paid field change
    paid: function(frm, cdt, cdn) {
       let gridRow = frm.open_grid_row();
       if (!gridRow) {
           gridRow = frm.get_field('wht_cert_detail').grid.get_row(cdn);
       }
       calWht(gridRow);
   },
    // event triggred when paid field change
    rate: function(frm, cdt, cdn) {
       let gridRow = frm.open_grid_row();
       if (!gridRow) {
           gridRow = frm.get_field('wht_cert_detail').grid.get_row(cdn);
       }
       calWht(gridRow);
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

/**
 * add filter to query
 * @param {object} frm - form object from frappe
 */
function setupWhtTypeQueries(frm) {
    frm.set_query('type', 'wht_cert_detail', function() {
        if (frm.doc.pnd) {
            let filterDict = {};
            let pnd = 'pnd' + frm.doc.pnd;
            filterDict[pnd] = 1;
            return {
                filters: filterDict,
            };
        } else {
            frappe.msgprint('กรุณาเลือก ภ.ง.ด.');
        }
    });
}

/**
 * calculate wht from rate and paid
 * @param {object} gridRow - row object of child table from frappe
 */
function calWht(gridRow) {
    let paid = gridRow.doc.paid;
    let rate = gridRow.doc.rate;

    if (typeof rate != 'undefined') {
        let wht = paid * (rate/100);
        frappe.model.set_value(
            gridRow.doc.doctype,
            gridRow.doc.name,
            'wht',
            wht
        );
    }
}
