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

        // override print function
        $('.fa-print').parent().unbind().click(function() {
            printPnd(frm);
        });
        $('a.grey-link:contains("'+__('Print')+'")').unbind().click(function() {
            printPnd(frm);
        });
        // add export function
        $('.fa-print').parents('span').before(`
            <span class="page-icon-group hidden-xs hidden-sm">
                <a class="text-muted no-decoration">
                    <i class="fa fa-list"></i>
                </a>
            </span>
        `)
        $('.fa-list').parent().click(function() {
            exportPnd(frm);
        });
        frm.page.add_menu_item(__('Internet Export'), function() {
            exportPnd(frm);
        });
    },
});


/** print pnd 
 * @param {object} frm
*/
function printPnd(frm) {
    let w = window.open(
        frappe.urllib.get_full_url(
            '/api/method/thai_wht.thai_wht.report.pnd_attach.pnd_attach.download_pdf_pnd?'
            + 'name=' + encodeURIComponent(frm.doc.name)
        )
    );
    if (!w) {
        frappe.msgprint(__('Please enable pop-ups')); return;
    }
}

/** export pnd txt file with | as seperator
 * @param {object} frm
*/
 async function exportPnd(frm) {
    const m = await frappe.call({
        method: 'thai_wht.thai_wht.report.' +
        'pnd_attach.pnd_attach.download_pdf_csv',
        async: true,
        args: {'name': frm.doc.name},
    });
    const data = m.message;
    const rowIndex = [
        'whdee',
        'whdee_prefix',
        'whdee_name',
        'date0',
        'type0',
        'rate0',
        'paid0',
        'wht0',
        'condition0',
        'date1',
        'type1',
        'rate1',
        'paid1',
        'wht1',
        'condition1',
        'date2',
        'type2',
        'rate2',
        'paid2',
        'wht2',
        'condition2',
    ];
    let dataList = [];
    for (let d=0; d<data.length; d++) {
        let row = [];
        for (let i=0; i<rowIndex.length; i++) {
            if (rowIndex[i] in data[d]) {
                row.push(data[d][rowIndex[i]]);
            } else {
                row.push('');
            }
        }
        let rowText = row.join('|');
        dataList.push(rowText);
    }
    let csvData = dataList.join('\r\n');

    let filename = frm.doc.name + '.txt';
    let a = document.createElement('a');

    let blobObject = new Blob([csvData], {type: 'text; charset=UTF-8'});
    a.href = URL.createObjectURL(blobObject);
    a.download = filename;

    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
