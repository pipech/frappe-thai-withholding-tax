// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Wht Cert', {
    onload: (frm) =>{
        if ($('#page-Form\\/Wht\\ Cert .octicon-mail').length===0) {
            $('#page-Form\\/Wht\\ Cert .fa-print').parents('span').before(`
                <span class="page-icon-group hidden-xs hidden-sm">
                    <a class="text-muted no-decoration">
                        <i class="octicon octicon-mail"></i>
                    </a>
                </span>
            `);
            $('.octicon-mail').parent().click(function() {
                printEnv(frm.doc.name);
            });
        }
    },
    refresh: function(frm) {
        // override print function
        $('.fa-print').parent().unbind().click(function() {
            printPDF();
        });
        $('a.grey-link:contains("'+__('Print')+'")').unbind().click(function() {
            printPDF();
        });

        setDefaultDate(frm);

        branchList.branchSelectionQuery(
            'Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch'
        );
        branchList.branchSelectionQuery(
            'Whdee', frm.doc.whdee, frm.doc.whdee_branch, 'whdee_branch'
        );

        frm.page.add_menu_item(__('Print Envelope'), function() {
            printEnv(frm.doc.name);
        });

        hideChildAddBtn(frm);
    },
    whder: function(frm) {
        branchList.branchSelectionQuery(
            'Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch'
        );
    },
    whdee: function(frm) {
        branchList.branchSelectionQuery(
            'Whdee', frm.doc.whdee, frm.doc.whdee_branch, 'whdee_branch'
        );
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
        hideChildAddBtn(frm);

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
 * hide add row button if wht child table have 3 entry
 * @param {object} frm
 */
function hideChildAddBtn(frm) {
    let hideBool;
    if (typeof(frm.doc.wht_cert_detail) == 'undefined') {
        hideBool = true;
    } else {
        hideBool = (frm.doc.wht_cert_detail.length < 3);
    }
    $('[data-fieldname="wht_cert_detail"] button.grid-add-row')
        .toggle(hideBool);
    $('[data-fieldname="wht_cert_detail"] button.grid-insert-row-below')
        .toggle(hideBool);
    $('[data-fieldname="wht_cert_detail"] button.grid-insert-row')
        .toggle(hideBool);
}

/**
 * open newtab and print pdf
 */
function printPDF() {
    let w = window.open(
        frappe.urllib.get_full_url(
            '/api/method/frappe.utils.print_format.download_pdf?'
            + 'doctype=' + encodeURIComponent(me.frm.doc.doctype)
            + '&name=' + encodeURIComponent(me.frm.doc.name)
            + '&format=Wht%20Certificate'
            + '&no_letterhead=0'
        )
    );
    if (!w) {
        frappe.msgprint(__('Please enable pop-ups')); return;
    }
}

/**
 * set default date for date field
 * @param {object} frm - form object from frappe
 */
function setDefaultDate(frm) {
    if (!frm.doc.date) {
        let today = frappe.datetime.nowdate();
        frm.set_value('date', today);
    };
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
            frappe.msgprint('?????????????????????????????? ???.???.???.');
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


/** print pnd 
 * @param {string} name
*/
function printEnv(name) {
    let w = window.open(
        frappe.urllib.get_full_url(
            '/api/method/thai_wht.utils.print_envelope.print_envelope?'
            + 'name=' + encodeURIComponent(name)
        )
    );
    if (!w) {
        frappe.msgprint(__('Please enable pop-ups')); return;
    }
}
