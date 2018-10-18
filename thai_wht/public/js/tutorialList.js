let tutorialDict = {
    addWhtCert: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="List/Wht Cert"]',
            content: 'กดที่นี่เพื่อเข้าสู่รายการหนังสือรับรอง',
            placement: 'top',
        },
        {
            pageLabel: 'List/Wht Cert',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'กดเพื่อสร้างหนังสือรับรอง',
            placement: 'top',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div[data-fieldname="pnd"] div.control-input > :first-child',
            content: 'กดเพื่อเลือกประเภท ภ.ง.ด.',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div[data-fieldname="whder"] div.awesomplete > :first-child',
            content: 'กดเพื่อเลือกผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div[data-fieldname="whdee"] div.awesomplete > :first-child',
            content: 'กดเพื่อเลือกผู้ถูกหักภาษี',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'button.grid-add-row',
            content: 'กดเพื่อเพิ่มรายละเอียดการจ่ายเงิน',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div[data-fieldname="type"] div.awesomplete > :first-child',
            content: 'กดเพื่อเลือกประเภทเงินได้',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div[data-fieldname="paid"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกจำนวนเงินที่จ่าย',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div[data-fieldname="rate"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกอัตราภาษีโดยไม่ต้องใส่ % เช่น กรอก 3 สำหรับอัตราภาษี 3%',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div.grid-header-toolbar button:has(span.octicon-triangle-up)',
            content: 'กดเพื่อปิดหน้าต่างรายละเอียดการจ่ายเงิน',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'กดเพื่อบันทึกรายการ',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'a:not(.hide) i.fa-print',
            content: 'กดเพื่อปริ้น และตรวจสอบ',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'button.btn-primary.dropdown-toggle:not(.hide)',
            content: 'เมื่อตรวจสอบเรียบร้อยแล้ว กดที่นี่',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'div.actions-btn-group ul.dropdown-menu > :first-child',
            content: 'กดเพื่อยืนยันเอกสาร',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'body > div.modal.fade.in button.btn-primary',
            content: 'กดเพื่อยืนยัน เอกสารที่ยืนยันแล้วไม่สามารถลบหรือแก้ไขได้',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'li a[href="#List/Wht Cert"]',
            content: 'กดเพื่อกลับไปที่รายการหนังสือรับรอง',
        },
        {
            pageLabel: 'List/Wht Cert',
            tippyElement: 'a.navbar-home',
            content: 'กดเพื่อกลับไปที่หน้าหลัก',
        },
    ],
    addPnd: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="modules/Thai Wht"]',
            content: 'กดที่นี่เพื่อเข้าสู่โมดูลภาษีหัก ณ ที่จ่าย',
            placement: 'top',
        },
        {
            pageLabel: 'Modules',
            tippyElement: 'div:has(>span.open-notification[data-doctype="Pnd"]) > :first-child',
            content: 'กดที่นี่เพื่อเข้าสู่รายการแบบยื่นรายการภาษี',
            placement: 'top',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'div.page-form.row button.btn-success',
            content: 'กดเพื่อสร้างแบบยื่นรายการภาษีอัตโนมัติ',
            placement: 'top',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'body > div.modal.fade.in button.btn-primary',
            content: 'กดเพื่อยืนยัน',
            placement: 'top',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'body > div.modal.fade.in button.btn-default',
            content: 'กดปิด',
            placement: 'top',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'div.result-list > div.list-items a.list-id',
            content: 'กดเพื่อเปิดเอกสารแบบยื่นรายการภาษี',
            placement: 'top',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'a:not(.hide) i.fa-print',
            content: 'กดเพื่อปริ้นเอกสาร',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'a:not(.hide) i.fa-list',
            content: 'กดเพื่อเซฟไฟล์สำหรับยื่นผ่านอินเตอร์เน็ต',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'เมื่อตรวจสอบเรียบร้อยแล้ว กดที่นี่',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'body > div.modal.fade.in button.btn-primary',
            content: 'กดเพื่อยืนยันเอกสาร เอกสารที่ยืนยันแล้วไม่สามารถลบหรือแก้ไขได้',
            placement: 'top',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'li a[href="#List/Pnd"]',
            content: 'กดเพื่อกลับไปที่รายการแบบยื่นรายการภาษี',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'a.navbar-home',
            content: 'กดเพื่อกลับไปที่หน้าหลัก',
        },
    ],
    addWhder: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="modules/Thai Wht"]',
            content: 'กดที่นี่เพื่อเข้าสู่โมดูลภาษีหัก ณ ที่จ่าย',
            placement: 'top',
        },
        {
            pageLabel: 'Modules',
            tippyElement: 'div:has(>span.open-notification[data-doctype="Whder"]) > :first-child',
            content: 'กดที่นี่เพื่อเข้าสู่รายการผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
            placement: 'top',
        },
        {
            pageLabel: 'List/Whder',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'กดเพื่อสร้างผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'div[data-fieldname="tax_id"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกเลขประจำตัวผู้เสียภาษี',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'div[data-fieldname="prefix"] div.awesomplete > :first-child',
            content: 'กดเพื่อเลือกคำนำหน้าชื่อ',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'div[data-fieldname="w_name"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกชื่อ',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'กดเพื่อบันทึกรายการ',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'button.btn-branch',
            content: 'กดเพื่อเพิ่มสาขา',
            placement: 'top',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="branch"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกเลขที่สาขา สำหรับสำนักงานใหญ่กรอก 0',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="address_line1"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกที่อยู่',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="sub_district"] span.twitter-typeahead > :nth-child(2)',
            content: 'กดเพื่อกรอกตำบล พร้อมเลือกอำเภอ และจังหวัด',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'กดเพื่อบันทึกรายการ',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'li a[href="#List/Whder"]',
            content: 'กดเพื่อกลับไปที่รายการผู้มีหน้าที่หักภาษี ณ ที่จ่าย',
        },
        {
            pageLabel: 'List/Whder',
            tippyElement: 'a.navbar-home',
            content: 'กดเพื่อกลับไปที่หน้าหลัก',
        },
    ],
    addWhdee: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="modules/Thai Wht"]',
            content: 'กดที่นี่เพื่อเข้าสู่โมดูลภาษีหัก ณ ที่จ่าย',
            placement: 'top',
        },
        {
            pageLabel: 'Modules',
            tippyElement: 'div:has(>span.open-notification[data-doctype="Whdee"]) > :first-child',
            content: 'กดที่นี่เพื่อเข้าสู่รายการผู้ถูกหักภาษี ณ ที่จ่าย',
            placement: 'top',
        },
        {
            pageLabel: 'List/Whdee',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'กดเพื่อสร้างผู้ถูกหักภาษี ณ ที่จ่าย',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'div[data-fieldname="tax_id"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกเลขประจำตัวผู้เสียภาษี',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'div[data-fieldname="prefix"] div.awesomplete > :first-child',
            content: 'กดเพื่อเลือกคำนำหน้าชื่อ',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'div[data-fieldname="w_name"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกชื่อ',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'กดเพื่อบันทึกรายการ',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'button.btn-branch',
            content: 'กดเพื่อเพิ่มสาขา',
            placement: 'top',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="branch"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกเลขที่สาขา สำหรับสำนักงานใหญ่กรอก 0',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="address_line1"] div.control-input > :first-child',
            content: 'กดเพื่อกรอกที่อยู่',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="sub_district"] span.twitter-typeahead > :nth-child(2)',
            content: 'กดเพื่อกรอกตำบล พร้อมเลือกอำเภอ และจังหวัด',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'กดเพื่อบันทึกรายการ',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'li a[href="#List/Whdee"]',
            content: 'กดเพื่อกลับไปที่รายการผู้ถูกหักภาษี ณ ที่จ่าย',
        },
        {
            pageLabel: 'List/Whdee',
            tippyElement: 'a.navbar-home',
            content: 'กดเพื่อกลับไปที่หน้าหลัก',
        },
    ],
    deleteDemo: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="delete_transaction"]',
            content: 'กดเพื่อลบข้อมูลตัวอย่าง',
            placement: 'top',
        },
        {
            pageLabel: 'Delete transaction',
            tippyElement: '#pwd',
            content: 'กดเพื่อกรอกรหัสผ่าน',
        },
        {
            pageLabel: 'Delete transaction',
            tippyElement: '#delete-demo',
            content: 'กดเพื่อยืนยันการลบข้อมูลตัวอย่าง',
        },
    ],
};
