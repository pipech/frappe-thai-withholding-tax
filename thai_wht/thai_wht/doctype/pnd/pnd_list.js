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
                        frappe.call({
                            method: 'thai_wht.thai_wht.doctype.pnd.pnd.autogen',
                            callback: function(message) {
                                console.log(message);
                                listview.refresh();
                            }
                        });
                    },
                );
            });
    },
};
