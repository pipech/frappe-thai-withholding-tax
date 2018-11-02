# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = 'thai_wht'
app_title = 'Thai Wht'
app_publisher = 'SpaceCode Co., Ltd.'
app_description = 'Thai Withholding tax'
app_icon = 'octicon octicon-repo-force-push'
app_color = 'green'
app_email = 'poranut@spacecode.co.th'
app_license = 'MIT'

after_install = 'thai_wht.setup.install.after_install'

app_include_js = [
    # format branch and tax_id input
    'assets/thai_wht/js/lib/cleave/cleave.min.js',
    # auto fill thai address
    'assets/thai_wht/js/lib/JQL.min.js',
    'assets/thai_wht/js/lib/typeahead.bundle.js',
    'assets/thai_wht/js/lib/jquery_thailand/jquery.Thailand.min.js',
    # list branch in form
    'assets/js/wht_branch.min.js',
    # tutorial
    'assets/thai_wht/js/lib/tippy/tippy.min.js',
    'assets/js/tutorial.min.js',
    # google analytics
    'assets/js/thai_wht_analytics.min.js',
    ]
app_include_css = [
    # auto fill thai address
    'assets/thai_wht/js/lib/jquery_thailand/jquery.Thailand.min.css',
    'assets/thai_wht/css/custom_tippy.css',
    ]

web_include_js = [
    '/assets/js/website.min.js',
    ]
web_include_css = '/assets/css/pnd_site.min.css'
website_context = {
    'brand_html': 'ภ.ง.ด.',
    'top_bar_items': [
        {'label': 'คู่มือการใช้งาน', 'url': 'https://docs.google.com/document/d/1JhlKvOL91ht_KA9BOscLQH9U9D2rQQ-Un2R3wgZIuhA/', 'right': 1},
        {'label': 'เข้าสู่ระบบ', 'url': '/login', 'right': 1},
    ],
    'hide_login': 1,
}
