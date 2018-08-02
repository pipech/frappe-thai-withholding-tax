# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "thai_wht"
app_title = "Thai Wht"
app_publisher = "SpaceCode Co., Ltd."
app_description = "Thai Withholding tax"
app_icon = "octicon octicon-repo-force-push"
app_color = "green"
app_email = "poranut@spacecode.co.th"
app_license = "MIT"

app_include_js = [
    # format branch and tax_id input
    'assets/thai_wht/js/lib/cleave/cleave.min.js',
    # auto fill thai address
    'assets/thai_wht/js/lib/JQL.min.js',
    'assets/thai_wht/js/lib/typeahead.bundle.js',
    'assets/thai_wht/js/lib/jquery_thailand/jquery.Thailand.min.js',
    # list branch in form
    'assets/js/wht_branch.min.js',
    ]

app_include_css = [
    # auto fill thai address
    'assets/thai_wht/js/lib/jquery_thailand/jquery.Thailand.min.css',
    ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/thai_wht/css/thai_wht.css"
# app_include_js = "/assets/thai_wht/js/thai_wht.js"

# include js, css files in header of web template
# web_include_css = "/assets/thai_wht/css/thai_wht.css"
# web_include_js = "/assets/thai_wht/js/thai_wht.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "thai_wht.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "thai_wht.install.before_install"
# after_install = "thai_wht.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thai_wht.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"thai_wht.tasks.all"
# 	],
# 	"daily": [
# 		"thai_wht.tasks.daily"
# 	],
# 	"hourly": [
# 		"thai_wht.tasks.hourly"
# 	],
# 	"weekly": [
# 		"thai_wht.tasks.weekly"
# 	]
# 	"monthly": [
# 		"thai_wht.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "thai_wht.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "thai_wht.event.get_events"
# }

