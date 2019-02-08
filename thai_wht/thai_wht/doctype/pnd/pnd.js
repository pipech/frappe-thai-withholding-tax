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
            $('.octicon-hubot').parent().click(function() {
                rdserverExportConfirm(frm.doc.name);
            });

            $('#page-Form\\/Pnd .fa-print').parents('span').before(`
                <span class="page-icon-group hidden-xs hidden-sm">
                    <a class="text-muted no-decoration">
                        <i class="fa fa-list"></i>
                    </a>
                </span>
            `);
            $('.fa-list').parent().click(function() {
                internetExportConfirm(frm.doc.name);
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
            internetExportConfirm(frm.doc.name);
        });
        frm.page.add_menu_item(__('RDserver Export'), function() {
            rdserverExportConfirm(frm.doc.name);
        });
    },
});

/** rdserver export confirm dialog
 * @param {string} name
*/
function internetExportConfirm(name) {
    frappe.confirm(
        `
        <p>
        ฟังก์ชั่นนี้ โปรแกรมจะทำการเซฟข้อมูล<br>
        ในรูปแบบที่ <b>ต้องทำการแปลงข้อมูลผ่าน โปรแกรมโอนย้ายข้อมูลภ.ง.ด. ของกรมสรรพากร</b><br>
        ก่อนที่จะนำไฟล์ที่ได้ไปยื่นผ่าน https://rdserver.rd.go.th
        </p>
        <p>
        วิธีการใช้<br>
        <ul>
            <li>ให้ท่านกดปุ่ม Yes สีฟ้าด้านบน</li>
            <li>
                ให้ท่านกดคลิ๊กขวาที่บริเวณที่มีข้อมูล จากนั้นเลือก Save as... และเซฟไฟล์ลงในโฟลเดอร์ที่ต้องการ<br>
                <small>
                    (สำหรับหลายๆท่าน ข้อมูลอาจะเป็นภาษาที่อ่านไม่ออก ไม่ต้องกังวล 
                    เมื่อนำข้อมูลไปยื่นผ่านโปรแกรมโอนย้ายข้อมูลเสร็จแล้ว 
                    ให้ท่านทดลองกด "พิมพ์" จะเห็นว่าข้อมูลเป็นภาษาไทยที่ถูกต้อง)
                    </small>
                </li>
            <li>
                นำไฟล์ที่ได้ ไปแปลงข้อมูลผ่าน โปรแกรมโอนย้ายข้อมูลภ.ง.ด. ของกรมสรรพากร
                <a href="https://docs.google.com/document/d/1JhlKvOL91ht_KA9BOscLQH9U9D2rQQ-Un2R3wgZIuhA/edit#heading=h.z2auia9i4ml" target="_blank">
                    กดที่นี่ เพื่อดูข้อมูลเพิ่มเติม
                </a>
            </li>
            <li>นำไฟล์ที่ได้จากโปรแกรมโอนย้ายข้อมูลภ.ง.ด. ไปยื่นผ่าน https://rdserver.rd.go.th</li>
        </ul>
        

        </p>
        `,
        function() {
            internetExportPnd(name);
        },
    );
}

/** rdserver export confirm dialog
 * @param {string} name
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
 * @param {object} name
*/
 async function internetExportPnd(name) {
    let w = window.open(
        frappe.urllib.get_full_url(
            '/api/method/thai_wht.thai_wht.report.pnd_attach.pnd_internet.download_csv?'
            + 'name=' + encodeURIComponent(name)
        )
    );
    if (!w) {
        frappe.msgprint(__('Please enable pop-ups')); return;
    }
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
