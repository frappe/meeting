# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "meeting"
app_title = "Meeting"
app_publisher = "Frappé"
app_description = "Prepare agenda, invite users and record minutes of a meeting"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@frappe.io"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting/css/meeting.css"
# app_include_js = "/assets/meeting/js/meeting.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting/css/meeting.css"
# web_include_js = "/assets/meeting/js/meeting.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Meeting"]

# Installation
# ------------

# before_install = "meeting.install.before_install"
# after_install = "meeting.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting.notifications.get_notification_config"

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

doc_events = {
	"User": {
		"after_insert": "meeting.api.make_orientation_meeting"
	},
	"ToDo": {
		"on_update": "meeting.api.update_minute_status",
		"on_trash": "meeting.api.update_minute_status"
	}
}

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
# 		"meeting.tasks.all"
# 	],
# 	"daily": [
# 		"meeting.tasks.daily"
# 	],
# 	"hourly": [
# 		"meeting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"meeting.tasks.weekly"
# 	]
# 	"monthly": [
# 		"meeting.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "meeting.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "meeting.event.get_events"
# }

