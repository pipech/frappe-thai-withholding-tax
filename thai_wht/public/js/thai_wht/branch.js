/** Render branch 
 * @param {object} frm
*/
function renderBranch(frm) {
    if (frm.fields_dict['branch_html'] && 'branch_list' in frm.doc.__onload) {
        $(frm.fields_dict['branch_html'].wrapper)
            .html(frappe.render_template('branch_list',
                cur_frm.doc.__onload))
            .find('.btn-branch').on('click', function() {
                frappe.new_doc('Wht Branch');
            });
    }
}

/** Clear branch 
 * @param {object} frm
*/
function clearBranch(frm) {
    $(frm.fields_dict['branch_html'].wrapper).html('');
}