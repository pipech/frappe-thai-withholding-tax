// Hack: skip all default frappe slides

frappe.provide('thai_wht.setup');

frappe.setup.on('before_load', function() {
    frappe.setup.slides = thai_wht.setup.slides_settings;
});

frappe.setup.on('after_load', function() {
    setTimeout(function() {
        $('.complete-btn').click();
    }, 1);
});

thai_wht.setup.slides_settings = [
    {

        name: 'slidesHack',
        title: __('ยินดีต้อนรับ'),
        fields: [],
        validate: function() {
            // insert frappe slide skiped value
            frappeSlideValue = {
                'language': 'English',
                'country': 'Thailand',
                'currency': 'THB',
                'timezone': 'Asia/Bangkok',
            };
            this.values = $.extend(this.values, frappeSlideValue);
            return true;
        },
    },
];
