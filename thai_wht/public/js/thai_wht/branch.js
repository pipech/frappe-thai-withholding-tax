branchList = {
    render: (frm) => {
        if (frm.fields_dict['branch_html'] && 'branch_list' in frm.doc.__onload) {
            $(frm.fields_dict['branch_html'].wrapper)
                .html(frappe.render_template('branch_list',
                    cur_frm.doc.__onload))
                .find('.btn-branch').on('click', function() {
                    frappe.new_doc('Wht Branch');
                });
        }
    },
    clear: (frm) => {
        $(frm.fields_dict['branch_html'].wrapper).html('');
    },
    redirect: () => {
        frappe.run_serially([
            () => frappe.timeout(1),
            () => {
                let lastRoute = frappe.route_history.slice(-2, -1)[0];
                if (frappe.dynamic_link && frappe.dynamic_link.doc
                    && frappe.dynamic_link.doc.name == lastRoute[2]) {
                    frappe.set_route(lastRoute[0], lastRoute[1], lastRoute[2]);
                } else {
                    let lastRoute = frappe.route_history.slice(-1)[0];
                    if (frappe.dynamic_link && frappe.dynamic_link.doc
                        && frappe.dynamic_link.doc.name == lastRoute[2]) {
                        frappe.set_route(lastRoute[0], lastRoute[1], lastRoute[2]);
                    }
                }
            },
        ]);
    },
    removeLocalLinks: (frm) => {
        if (frm.doc.links) {
            frm.doc.links.forEach(function(d) {
                frappe.model.remove_from_locals(d.link_doctype, d.link_name);
            });
        }
    },
    autoFill: (frm) => {
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
};
