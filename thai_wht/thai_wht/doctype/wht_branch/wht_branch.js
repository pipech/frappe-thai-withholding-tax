// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

let thaiAutoFillloaded = 0;

frappe.ui.form.on('Wht Branch', {
    onload: function(frm) {
        // thai address auto fill
        if (thaiAutoFillloaded === 0) {
            thaiAutoFillloaded = 1;

            $.Thailand({
                $district: $('[data-fieldname="sub_district"] input'),
                $amphoe: $('[data-fieldname="district"] input'),
                $province: $('[data-fieldname="province"] input'),
                $zipcode: $('[data-fieldname="zip_code"] input'),
            });
        }
    },
    refresh: function(frm) {
        // format branch input
        if (frm.doc.__islocal) {
            frm.cleave = {};
            frm.cleave.branch = new Cleave(
                $('[data-fieldname="branch"] input').last(),
                {
                    numericOnly: true,
                    blocks: [5],
                }
            );
        }
        branchList.autoFill(frm);
    },
    validate: function(frm) {
        branchList.removeLocalLinks(frm);
    },
    after_save: function(frm) {
        branchList.redirect();
    },
});
