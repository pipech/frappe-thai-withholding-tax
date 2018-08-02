// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

let loaded = 0;

frappe.ui.form.on('Wht Branch', {
    onload: function(frm) {
        // thai address auto fill
        
        if (loaded === 0) {
            loaded = 1;

            $.Thailand({
                $district: $('[data-fieldname="sub_district"] input'),
                $amphoe: $('[data-fieldname="district"] input'),
                $province: $('[data-fieldname="province"] input'),
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

        // auto fill link field 1/3
        if (frm.doc.__islocal) {
            let lastRoute = frappe.route_history.slice(-2, -1)[0];
            let docname = lastRoute[2];
            if (lastRoute.length > 3) {
                docname = lastRoute.slice(2).join('/');
            }
            if (frappe.dynamic_link && frappe.dynamic_link.doc
                    && frappe.dynamic_link.doc.name==docname) {
                frm.add_child('links', {
                    link_doctype: frappe.dynamic_link.doctype,
                    link_name: frappe.dynamic_link.doc[frappe.dynamic_link.fieldname],
                });
            }
        }
        frm.set_query('link_doctype', 'links', function() {
            return {
                query: 'frappe.contacts.address_and_contact.filter_dynamic_link_doctypes',
                filters: {
                    fieldtype: 'HTML',
                    fieldname: 'address_html',
                },
            };
        });
        frm.refresh_field('links');
    },
    validate: function(frm) {
        // auto fill link field 2/3
        if (frm.doc.links) {
            frm.doc.links.forEach(function(d) {
                frappe.model.remove_from_locals(d.link_doctype, d.link_name);
            });
        }
    },
    after_save: function() {
        // auto fill link field 3/3
        frappe.run_serially([
            () => frappe.timeout(1),
            () => {
                let lastRoute = frappe.route_history.slice(-2, -1)[0];
                if (frappe.dynamic_link && frappe.dynamic_link.doc
                    && frappe.dynamic_link.doc.name == lastRoute[2]) {
                    frappe.set_route(lastRoute[0], lastRoute[1], lastRoute[2]);
                }
            },
        ]);
    },
});
