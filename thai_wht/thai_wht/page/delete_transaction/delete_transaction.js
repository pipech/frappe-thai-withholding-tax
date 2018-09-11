checkPassword();

/** check password 
 * @param {text} title
 * @param {text} description
*/
function checkPassword(title, description) {
    let _title;
    if (title) {
        _title = title;
    } else {
        _title = __('ลบข้อมูลตัวอย่างทั้งหมด');
    }

    let _description;
    if (description) {
        _description = description;
    } else {
        _description = __('กรุณากรอกพาสเวิร์ด เพื่อยืนยัน การลบข้อมูลตัวอย่าง เมื่อลบข้อมูลตัวอย่างแล้ว เอกสารที่ Sutmit แล้วจะไม่สามารถลบข้อมูลได้ กรุณาตรวจสอบข้อมูลก่อน Submit เอกสาร');
    }

    let p = frappe.prompt(
        {
            fieldname: 'password',
            fieldtype: 'Password',
            reqd: 1,
            label: __('กรุณากรอกพาสเวิร์ด เพื่อยืนยัน'),
            description: _description,
        },
        (data) => {
            frappe.call({
                method: 'thai_wht.setup.demo.check_password',
                args: {
                    pwd: data.password,
                },
                callback: function(r) {
                    if (r.message == 'wrong password') {
                        checkPassword(__('พาสเวิร์ดไม่ถูกต้อง'), __('พาสเวิร์ดผิดพลาด กรุณากรอกพาสเวิร์ดใหม่อีกครั้ง'));
                    } else {
                        frappe.msgprint(`
                        <b>ระบบกำลังลบข้อมูลตัวอย่างอยู่</b><br>
                        <p>กรุณาอย่าปิด หรือกดรีเฟรช</p>`
                        , 'กรุณารอสักครู่');
                        deleteTransaction();
                    }
                },
            });
        },
        _title,
        __('Delete'),
    );
    p.get_primary_btn().addClass('btn-danger');
    $('div.modal-backdrop').next().find('.btn-modal-close').click(() => {
        window.location.href = '/desk';
    });
}

/** call delete transaction */
function deleteTransaction() {
    frappe.call({
        method: 'thai_wht.setup.demo.delete_transaction',
        freeze: true,
        callback: function(r) {
            if (!r.exc) {
                frappe.msgprint(__('ลบข้อมูลตัวอย่างเสร็จเรียบร้อย'));
                setTimeout(() => {
                    window.location.href = '/desk';
                }, 1000);
            } else {
                frappe.msgprint(`
                <b>เกิดข้อผิดพลาด</b><br>
                <p>Error : การลบข้อมูลตัวอย่างไม่สำเร็จ</p>
                <br>
                <p>สอบถามเพิ่มเติม กรุณาติดต่อ : help@pnd.in.th</p>`
                , 'มีข้อผิดพลาด');
            }
            $('div.modal-backdrop').next().find('.btn').click(() => {
                window.location.href = '/desk';
            });
        },
    });
}