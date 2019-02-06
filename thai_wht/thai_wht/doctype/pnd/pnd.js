// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pnd', {
    whder: function(frm) {
        branchList.branchSelectionQuery(
            'Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch'
        );
    },
    onload: (frm) =>{
        if ($('#page-Form\\/Pnd .fa-list').length===0) {
            // add export function
            $('#page-Form\\/Pnd .fa-print').parents('span').before(`
                <span class="page-icon-group hidden-xs hidden-sm">
                    <a class="text-muted no-decoration">
                        <i class="octicon octicon-hubot"></i>
                    </a>
                </span>
            `);
            $('#page-Form\\/Pnd .fa-print').parents('span').before(`
                <span class="page-icon-group hidden-xs hidden-sm">
                    <a class="text-muted no-decoration">
                        <i class="fa fa-list"></i>
                    </a>
                </span>
            `);
            $('.fa-list').parent().click(function() {
                exportPnd(frm);
            });
            $('.octicon-hubot').parent().click(function() {
                rdserverExportConfirm(frm.doc.name);
            });
        }
    },
    refresh: (frm) => {
        branchList.branchSelectionQuery(
            'Whder', frm.doc.whder, frm.doc.whder_branch, 'whder_branch'
        );

        // override print function
        $('.fa-print').parent().unbind().click(function() {
            printPnd(frm.doc.name);
        });
        $('a.grey-link:contains("'+__('Print')+'")').unbind().click(function() {
            printPnd(frm.doc.name);
        });
        // added export menu function
        frm.page.add_menu_item(__('Internet Export'), function() {
            exportPnd(frm);
        });
        frm.page.add_menu_item(__('RDserver Export'), function() {
            rdserverExportConfirm(frm.doc.name);
        });
    },
});

/** rdserver export confirm dialog
 *  * @param {string} name
*/
function rdserverExportConfirm(name) {
    frappe.confirm(
        `
        <p>
        ฟังก์ชั่นนี้ โปรแกรมจะทำการเซฟข้อมูลในรูปแบบที่สามารถยื่นผ่าน
        https://rdserver.rd.go.th ได้โดยตรง โดยไม่ต้องผ่านโปรแกรมโอนย้ายข้อมูลภ.ง.ด.
        </p>
        <p><b>
        ฟังก์ชั่นนี้ อยู่ในขั้นทดลอง ทาง https://pnd.in.th 
        ไม่ขอรับผิดชอบความเสียหายที่อาจเกิดจากข้อมูลที่นำส่งผิดพลาดใดๆทั้งสิ้น
        </b></p>
        <p>
        ท่านต้องการดำเนินการต่อหรือไม่ ?
        </p>
        <p>
        หากไม่ต้องการ ท่านยังสามารถนำส่งข้อมูลภาษีได้ 2 วิธี คือ
        <ol>
            <li>นำส่งด้วยตนเอง กดที่ปุ่ม <i class="fa fa-print"></i></li> 
            <li>นำส่งด้วยอินเตอร์เน็ต ผ่านโปรแกรมโอนย้ายข้อมูลภ.ง.ด. 
            กดที่ปุ่ม <i class="fa fa-list"></i></li> 
        </ol>
        </p>
        `,
        function() {
            webExportPnd(name);
        },
    );
}

/** print pnd 
 * @param {string} name
*/
function printPnd(name) {
    let w = window.open(
        frappe.urllib.get_full_url(
            '/api/method/thai_wht.thai_wht.report.pnd_attach.pnd_paper.download?'
            + 'name=' + encodeURIComponent(name)
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

/** export pnd txt file with | as seperator
 * @param {string} name
*/
function webExportPnd(name) {
    let w = window.open(
        frappe.urllib.get_full_url(
            '/api/method/thai_wht.thai_wht.report.pnd_attach.pnd_internet.download?'
            + 'name=' + encodeURIComponent(name)
        )
    );
    if (!w) {
        frappe.msgprint(__('Please enable pop-ups')); return;
    }
}
