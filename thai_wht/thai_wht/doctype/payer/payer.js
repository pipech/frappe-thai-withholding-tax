// Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payer', {
    refresh: function(frm) {
        frm.set_query('prefix', function() {
            return {
                'filters': [
                    ['type', '=', 'Ind'],
                    ['prefix', '!=', 'หสม.'],
                ],
            };
        });
    },
});
