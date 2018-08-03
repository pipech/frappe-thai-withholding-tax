// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Wht Cert', {
    refresh: function(frm) {
        setDefaultDate(frm);
        branchList.branchSelectionQuery('Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch');
        branchList.branchSelectionQuery('Whdee', frm.doc.whdee, frm.doc.whdee_branch, 'whdee_branch');
    },
    whder: function(frm) {
        branchList.branchSelectionQuery('Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch');
    },
    whdee: function(frm) {
        branchList.branchSelectionQuery('Whdee', frm.doc.whdee, frm.doc.whdee_branch, 'whdee_branch');
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
