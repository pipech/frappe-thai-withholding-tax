frappe.listview_settings['Pnd'] = {
    onload: function(listview) {
        $('button.btn-primary.primary-action:contains('+__('New')+')').after(`
            <button class="btn btn-success">
                <i class="visible-xs octicon octicon-versions "></i>
                <span class="hidden-xs">`+__('Auto Generate')+`</span>
            </button>
        `);
        $('button.btn-success:contains('+__('Auto Generate')+')')
            .click(function() {
                frappe.confirm(
                    'Auto Generate ?',
                    function() {
                        alert('hhh')
                        // frappe.call({
                        //     method:'frappe.core.doctype.error_log.error_log.clear_error_logs',
                        //     callback: function() {
                        //         listview.refresh();
                        //     }
                        // });
                    },
                );
            });
    },
};
