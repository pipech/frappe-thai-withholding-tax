frappe.listview_settings['Pnd'] = {
    onload: function(listview) {
        setTimeout(() => {
            createAutoGenButton();
        }, 1);
    },
};

/** Create auto gen button */
function createAutoGenButton() {
    $('#page-List\\/Pnd .octicon-search.text-muted')
        .next('div.form-group.frappe-control')
        .after(`
                <style>
                @media (max-width: 767px) {
                    .remove-margin-xs {
                        margin-right: 0px !important;
                    }
                }
            </style>
            <div 
                class="col-md-2 text-right" 
                style="position: absolute; right: 0px;"
                >
                <button 
                    class="btn btn-success remove-margin-xs" 
                    style="margin-right: 15px;"
                    >
                    <i class="visible-xs octicon octicon-versions "></i>
                    <span class="hidden-xs">Auto</span>
                </button>
            </div>
        `);
    $('button.btn-success:contains('+__('Auto')+')')
        .click(function() {
            frappe.confirm(
                'Auto Generate ?',
                function() {
                    frappe.call({
                        method: 'thai_wht.thai_wht.doctype.pnd.pnd.autogen',
                        callback: function(r) {
                            frappe.msgprint(r.message);
                            // this might change soon
                            // might not need true parameters
                            cur_list.refresh(true);
                        },
                    });
                },
            );
        });
}