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
            content: 'กดเพื่อยืนยัน',
        },
        {
            pageLabel: 'Form/Wht Cert',
            tippyElement: 'li a[href="#List/Wht Cert"]',
            content: 'กดเพื่อกลับไปที่รายการหนังสือรับรอง',
        },
    ],
    addPnd: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="modules/Thai Wht"]',
            content: 'เพ่กดโตงเน้นะคร้าบ จะได้ไปออกหนังสือรับรอง',
        },
        {
            pageLabel: 'Modules',
            tippyElement: 'div:has(>span.open-notification[data-doctype="Pnd"]) > :first-child',
            content: 'ไปสร้างภงดจ้า',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'div.page-form.row button.btn-success',
            content: 'ออโต้เจ็นจ้า',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'body > div.modal.fade.in button.btn-primary',
            content: 'เย็ดแน่นวน',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'body > div.modal.fade.in button.btn-default',
            content: 'ปิดปิด',
        },
        {
            pageLabel: 'List/Pnd',
            tippyElement: 'div.result-list > div.list-items a.list-id',
            content: 'เปิดด๊อก',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'a:not(.hide) i.fa-print',
            content: 'กดอันนี้เพื่อปริ้นเป็นกระดาษ',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'a:not(.hide) i.fa-list',
            content: 'กดอันนี้เพื่อปริ้นทางเน็ต คุณยังต้องไปยื่นเองอยู่ดีนะ',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'กรุณาตรวจสอบให้ดี เมื่อยืนยันแล้วลบบ่ได้เด๊อ',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'body > div.modal.fade.in button.btn-primary',
            content: 'กรุณาตรวจสอบให้ดี เมื่อยืนยันแล้วลบบ่ได้เด๊อ',
        },
        {
            pageLabel: 'Form/Pnd',
            tippyElement: 'li a[href="#List/Pnd"]',
            content: 'กดโตงนี้เพื่อกลับปายคร้าบเพ่',
        },
    ],
    addWhder: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="modules/Thai Wht"]',
            content: 'เพ่กดโตงเน้นะคร้าบ ผู้มีหน้าที่',
        },
        {
            pageLabel: 'Modules',
            tippyElement: 'div:has(>span.open-notification[data-doctype="Whder"]) > :first-child',
            content: 'เพ่กดโตงเน้นะคร้าบ ผู้มีหน้าที่หักภาษี',
        },
        {
            pageLabel: 'List/Whder',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'เพ่กดโตงเน้นะคร้าบ สร้างค้าบเพ่สร้างงง',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'div[data-fieldname="tax_id"] div.control-input > :first-child',
            content: 'กรอกเลข เป็นตัวเลข',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'div[data-fieldname="prefix"] div.awesomplete > :first-child',
            content: 'กรอกคำนำหน้าชื่อ',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'div[data-fieldname="w_name"] div.control-input > :first-child',
            content: 'กรอกชื่อ',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'เสร็จแล้วก็เซฟค้าบเพ่',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'button.btn-branch',
            content: 'เพิ่มสาขาจ้า',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="branch"] div.control-input > :first-child',
            content: 'กรอกสาขาเป็นตัวเลข 0 สำหรับสำนักงานใหญ่',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="address_line1"] div.control-input > :first-child',
            content: 'กรอกที่อยู่',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="sub_district"] span.twitter-typeahead > :nth-child(2)',
            content: 'กรอกตำบล พร้อมเลือกอำเภอ และจังหวัด',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'เสร็จแล้วก็เซฟสาขาค้าบเพ่',
        },
        {
            pageLabel: 'Form/Whder',
            tippyElement: 'li a[href="#List/Whder"]',
            content: 'กดโตงนี้เพื่อกลับปายคร้าบเพ่',
        },
    ],
    addWhdee: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="modules/Thai Wht"]',
            content: 'เพ่กดโตงเน้นะคร้าบ ผู้มีหน้าที่',
        },
        {
            pageLabel: 'Modules',
            tippyElement: 'div:has(>span.open-notification[data-doctype="Whdee"]) > :first-child',
            content: 'เพ่กดโตงเน้นะคร้าบ ผู้มีหน้าที่หักภาษี',
        },
        {
            pageLabel: 'List/Whdee',
            tippyElement: 'button.btn-primary.primary-action:not(.hide)',
            content: 'เพ่กดโตงเน้นะคร้าบ สร้างค้าบเพ่สร้างงง',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'div[data-fieldname="tax_id"] div.control-input > :first-child',
            content: 'กรอกเลข เป็นตัวเลข',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'div[data-fieldname="prefix"] div.awesomplete > :first-child',
            content: 'กรอกคำนำหน้าชื่อ',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'div[data-fieldname="w_name"] div.control-input > :first-child',
            content: 'กรอกชื่อ',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'เสร็จแล้วก็เซฟค้าบเพ่',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'button.btn-branch',
            content: 'เพิ่มสาขาจ้า',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="branch"] div.control-input > :first-child',
            content: 'กรอกสาขาเป็นตัวเลข 0 สำหรับสำนักงานใหญ่',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="address_line1"] div.control-input > :first-child',
            content: 'กรอกที่อยู่',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'div[data-fieldname="sub_district"] span.twitter-typeahead > :nth-child(2)',
            content: 'กรอกตำบล พร้อมเลือกอำเภอ และจังหวัด',
        },
        {
            pageLabel: 'Form/Wht Branch',
            tippyElement: 'button.btn-primary.primary-action:not(.hide):has(i.octicon-check)',
            content: 'เสร็จแล้วก็เซฟสาขาค้าบเพ่',
        },
        {
            pageLabel: 'Form/Whdee',
            tippyElement: 'li a[href="#List/Whdee"]',
            content: 'กดโตงนี้เพื่อกลับปายคร้าบเพ่',
        },
    ],
    deleteDemo: [
        {
            pageLabel: 'Desktop',
            tippyElement: 'div.case-wrapper[data-link="delete_transaction"]',
            content: 'เพ่กดโตงเน้นะคร้าบ ผู้มีหน้าที่',
        },
        {
            pageLabel: 'Delete transaction',
            tippyElement: '#pwd',
            content: 'กรอกพาสสะเวิ้ด',
        },
        {
            pageLabel: 'Delete transaction',
            tippyElement: '#delete-demo',
            content: 'กดยืนยัน',
        },
    ],
};
