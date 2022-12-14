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
        ???????????????????????????????????? ?????????????????????????????????????????????????????????????????????<br>
        ????????????????????????????????? <b>????????????????????????????????????????????????????????????????????? ???????????????????????????????????????????????????????????????.???.???. ???????????????????????????????????????</b><br>
        ????????????????????????????????????????????????????????????????????????????????????????????? https://rdserver.rd.go.th
        </p>
        <p>
        ??????????????????????????????<br>
        <ul>
            <li>??????????????????????????????????????? Yes ?????????????????????????????????</li>
            <li>
                ??????????????????????????????????????????????????????????????????????????????????????????????????????????????? ???????????????????????????????????? Save as... ????????????????????????????????????????????????????????????????????????????????????????????????<br>
                <small>
                    (????????????????????????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????? ???????????????????????????????????? 
                    ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 
                    ?????????????????????????????????????????? "???????????????" ????????????????????????????????????????????????????????????????????????????????????????????????????????????)
                    </small>
                </li>
            <li>
                ???????????????????????????????????? ???????????????????????????????????????????????? ???????????????????????????????????????????????????????????????.???.???. ???????????????????????????????????????
                <a href="https://docs.google.com/document/d/1JhlKvOL91ht_KA9BOscLQH9U9D2rQQ-Un2R3wgZIuhA/edit#heading=h.z2auia9i4ml" target="_blank">
                    ???????????????????????? ??????????????????????????????????????????????????????????????????
                </a>
            </li>
            <li>????????????????????????????????????????????????????????????????????????????????????????????????????????????.???.???. ?????????????????????????????? https://rdserver.rd.go.th</li>
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
        ???????????????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        https://rdserver.rd.go.th ??????????????????????????? ?????????????????????????????????????????????????????????????????????????????????????????????????????????.???.???.
        </p>
        <p><b>
        ???????????????????????????????????? ????????????????????????????????????????????? ????????? https://pnd.in.th 
        ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        </b></p>
        <p>
        ?????????????????????????????????????????????????????????????????????????????????????????? ?
        </p>
        <p>
        ??????????????????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????? 2 ???????????? ?????????
        <ol>
            <li>?????????????????????????????????????????? ??????????????????????????? <i class="fa fa-print"></i></li> 
            <li>??????????????????????????????????????????????????????????????? ???????????????????????????????????????????????????????????????????????????.???.???. 
            ??????????????????????????? <i class="fa fa-list"></i></li> 
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
