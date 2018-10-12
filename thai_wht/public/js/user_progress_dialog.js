frappe.ui.toolbar.Toolbar.prototype.setup_progress_dialog = function() {
    console.log('hahaha lololo')
    frappe.call({
        method: 'frappe.desk.user_progress.get_user_progress_slides',
        callback: function(r) {
            if (r.message) {
                let slides = r.message;
                if (slides.length && slides.map((s) => parseInt(s.done)).includes(0)) {
                    frappe.require('assets/frappe/js/frappe/ui/toolbar/user_progress_dialog.js', function() {

                        let progressDialog = new frappe.setup.UserProgressDialog({
                            slides: slides,
                        });
                        $('.user-progress').removeClass('hide');
                        $('.user-progress .dropdown-toggle').on('click', () => {
                            progressDialog.show();
                        });

                        if (cint(frappe.boot.sysdefaults.is_first_startup)) {
                            progressDialog.show();
                            frappe.call({
                                method: 'frappe.desk.page.setup_wizard.setup_wizard.reset_is_first_startup',
                                args: {},
                                callback: () => {},
                            });
                        }

                    });
                }
            }
        },
        freeze: false,
    });
};
