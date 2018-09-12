frappe.pages['delete_transaction'].on_page_load = function(wrapper) {
    $('#page-delete_transaction').append(frappe.templates.frappe_box);
    $('#page-delete_transaction').append(frappe.templates.delete_transaction);

    // blur event password
    $('#pwd').on('blur', function() {
        let pwd = $(this).val();
        validateSingleForm('pwd', pwd);
    });

    // hide-show password
    let mask = true;
    $('#pass-toggle').on('click', () => {
        if (mask) {
            $('#pwd').attr('type', 'text');
            mask = false;
        } else {
            $('#pwd').attr('type', 'password');
            mask = true;
        }
    });

    // form submit
    $('#delete-demo-form').submit(function(evt) {
        evt.preventDefault();
        let pwd = $('#pwd').val();
        validateSingleForm('pwd', pwd);

        // check for error
        let err = $('div.form-group').hasClass('has-error');
        if (err) {
            return;
        }

        // check password
        frappe.call({
            method: 'thai_wht.setup.demo.check_password',
            args: {
                'pwd': pwd,
            },
            callback: function(r) {
                if (r.message == 'wrong password') {
                    addRemoveErr('pwd', 'พาสเวิร์ดไม่ถูกต้อง');
                    return;
                } else {
                    startRealtimeUpdate();
                    callDeleteDemo(pwd);
                }
            },
        });
    });

    $('#cancel-demo').click(() => {
        window.location.href = '/desk';
    });
};

/** Call python delete function 
 * @param {text} pwd
*/
function callDeleteDemo(pwd) {
    frappe.call({
        method: 'thai_wht.setup.demo.delete_demo',
        args: {
            'pwd': pwd,
        },
        callback: (r) => {
            let m = r.message;
            if (m.status === 'ok') {
                let indicator = 'success';
                let bodyHtml = '<p>Demo deletion success</p>';
                let percent = '100';
                updateFrappeBox(indicator, percent, bodyHtml);
                setTimeout(() => {
                    window.location.href = '/desk';
                }, 5000);
            } else {
                let indicator = 'error';
                let bodyHtml = '<p>' + r.message.fail + '</p>';
                let percent = '100';
                updateFrappeBox(indicator, percent, bodyHtml);
            }
        },
    });
}

/** Hide form, show update */
function startRealtimeUpdate() {
    // toggle dialog
    $('table.demo-form').hide();
    $('table.demo-update').show();

    frappe.realtime.on('delete_demo', (data) => {
        console.log('data', data);
        let indicator = 'success';
        let bodyHtml = '<p>' + data.stage_status + '</p>';
        let percent = String(Math.round((data.progress[0] / data.progress[1]) * 100));
        updateFrappeBox(indicator, percent, bodyHtml);
    });
}

/** Update data on frappe box using jquery
 * @param {string} indicator
 * @param {string} percent
 * @param {string} bodyHtml
 */
function updateFrappeBox(indicator, percent, bodyHtml) {
    let progressBar = $('#box_progress_bar');
    let boxBody = $('#box_body');
    // update process bar
    let percentText;
    if (percent === '0') {
        percentText = '';
        percent = 10;
    } else {
        percentText = percent + '%';
    }
    progressBar.attr('aria-valuenow', percent);
    progressBar.css('width', percent + '%');
    progressBar.text(percentText);
    // update body
    boxBody.html(bodyHtml);
    // toggle to error
    if (indicator === 'error') {
        // update indicator
        let indicatorBtn = $('#indicator_button');
        indicatorBtn.removeClass('indicator-green');
        indicatorBtn.addClass('indicator-red');
        // update process bar
        // process bar color
        progressBar.removeClass('progress-bar-success');
        progressBar.addClass('progress-bar-danger');
        progressBar.text('');
        // remove please wait text
        $('#please_wait_text').html(`
            <p>มีข้อผิดพลาด : กรุณาติดต่อ help@pnd.in.th</p>
        `);
        // update header
        let boxHeader = $('#box-header-text');
        boxHeader.text('Error');
    }
};

/** Validate Single Form input 
 * @param {string} id
 * @param {string} val
*/
function validateSingleForm(id, val) {
    if (validate[id]) {
        let err = validate[id](val);
        addRemoveErr(id, err);
    }
}

/** Add or remove error
 * @param {string} id
 * @param {string} err
*/
function addRemoveErr(id, err) {
    // change id class
    if (err.length > 0) {
        $('div.'+id).addClass('has-error');
        $('div.'+id).children('span').text(err);
    } else {
        $('div.'+id).removeClass('has-error');
        $('div.'+id).children('span').text('');
    }
}

const validate = {
    pwd: (pwd, subdomain='') => {
        let err = [];
        if (pwd == '') {
            err.push('กรุณากรอก พาสเวิร์ด');
            return err;
        };
        if (pwd.length < 8 || pwd.length > 30) {
            err.push('พาสเวิร์ด ต้องมีความยาว 8-30 ตัวอักษรเท่านั้น');
            return err;
        }
        if (subdomain) {
            if (pwd == subdomain) {
                err.push('พาสเวิร์ด ต้องแตกต่างจาก ชื่อ หรือ ตัวย่อ บริษัท ภาษาอังกฤษ');
                return err;
            }
        }
        re = /^[\w\d !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]+$/;
        if (!re.test(pwd)) {
            err.push('พาสเวิร์ด ต้องเป็นตัวอักษรภาษาอังกฤษ หรือตัวเลข หรืออักษร !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ เท่านั้น');
            return err;
        }
        let contain = [];
        re = /[0-9]/;
        if (!re.test(pwd)) {
            contain.push('ตัวเลข[0-9]');
        }
        re = /[a-z]/;
        if (!re.test(pwd)) {
            contain.push('ตัวอักษรเล็กภาษาอังกฤษ[a-z]');
        }
        re = /[A-Z]/;
        if (!re.test(pwd)) {
            contain.push('ตัวอักษรใหญ่ภาษาอังกฤษ[A-Z]');
        }
        if (contain.length > 0) {
            err.push('พาสเวิร์ด ต้องประกอบไปด้วย ตัวเลข[0-9] ตัวอักษรเล็กภาษาอังกฤษ[a-z] ตัวอักษรใหญ่ภาษาอังกฤษ[A-Z] อย่างน้อยอย่างละ 1 ตัว');
            return err;
        }
        return err;
    },
};
