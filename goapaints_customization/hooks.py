from . import __version__ as app_version

app_name = "goapaints_customization"
app_title = "Goa Paints"
app_publisher = "Raj Tailor"
app_description = "Goa Paints Personal CUstomization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tailorraj111@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/goapaints_customization/css/goapaints_customization.css"
# app_include_js = "/assets/goapaints_customization/js/goapaints_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/goapaints_customization/css/goapaints_customization.css"
# web_include_js = "/assets/goapaints_customization/js/goapaints_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "goapaints_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Production Plan" :["custom_scripts/production_plan.js"],
	"Stock Entry":[ "custom_scripts/stock_entry.js"],
	"Work Order":["custom_scripts/work_order.js"],
	"Item":["custom_scripts/item.js"],
	"Quality Inspection Template":["custom_scripts/quality_inspection_template.js"],
	"BOM":["custom_scripts/bom.js"],
	"Material Request":["custom_scripts/material_request.js"],
	"Sales Order":["custom_scripts/sales_order.js"],
    "Opportunity":["custom_scripts/opportunity.js"],
    "Quotation":["custom_scripts/quotation.js"]
	}
# doctype_js = {
#     "BOM": "custom_scripts/bom.js",
# 	"Material Request":["goa_paints/custom_doctype/Material_Request/material_request.js"]
# }
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "goapaints_customization.install.before_install"
# after_install = "goapaints_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "goapaints_customization.uninstall.before_uninstall"
# after_uninstall = "goapaints_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "goapaints_customization.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Production Plan":{
		"validate": "goapaints_customization.goa_paints.custom_doctype.production_plan.production_plan.before_insert"
	},
	"BOM":{
		"on_submit": "goapaints_customization.goa_paints.custom_doctype.BOM.bom.on_submit",
		"validate": "goapaints_customization.goa_paints.custom_doctype.BOM.bom.validate"
	},
	"Work Order":{
		"validate": "goapaints_customization.goa_paints.custom_doctype.Work_Order.work_order.validate"
	},
	"Stock Entry":{
		"validate":"goapaints_customization.goa_paints.custom_doctype.stock_entry.stock_entry.validate"
	},
	"Quality Inspection":{
		"on_submit":"goapaints_customization.goa_paints.custom_doctype.Quality_Inspection.quality_inspection.validate"
	},
	"Quality Inspection":{
		"on_submit":"goapaints_customization.goa_paints.custom_doctype.Quality_Inspection.quality_inspection.validate"
	},
	"Quotation":{
		"on_trash":"goapaints_customization.goa_paints.custom_doctype.Quotation.quotation.on_trash",
        "validate":"goapaints_customization.goa_paints.custom_doctype.Quotation.quotation.validate"
	},
	"Item":{
		"validate":"goapaints_customization.goa_paints.custom_doctype.Item.item.validate"
	},
    "Salary Slip":{
		"validate":"goapaints_customization.goa_paints.custom_doctype.salary_slip.salary_slip.validate",
        "after_insert":"goapaints_customization.goa_paints.custom_doctype.salary_slip.salary_slip.after_insert"
	}
}

fixtures = ["Workflow State","Workflow Action Master",
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", ["Production Plan Sub Assembly Item-item_category_custom","Stock Entry-process_loss_perc","Work Order-employee_2","Work Order-employee_1","Work Order-current_wo_status","BOM-volume_solid_percent","BOM-total_volume_solid_qty","BOM Item-volume_solid_qty","BOM Item-volume_solid_percent","Stock Entry-quality_inspection_custom","BOM Item-item_category_custom","Quality Inspection Parameter-unit","Work Order-total_weight","Work Order-last_batch","BOM-total_weight","Stock Entry-sfg_batch_no","Item-sfg_item_reference","Work Order-density","Work Order-total_volume","BOM-density","BOM-total_volume","Stock Entry-output_litre","Stock Entry-specific_gravity","Quality Inspection Reading-is_process_parameter","Item Quality Inspection Parameter-is_process_parameter","Stock Entry Detail-specific_gravity","Work Order-is_process_bom","Quality Inspection Reading-test_standard","Quality Inspection Reading-units","Quality Inspection Reading-average_value_","Item Quality Inspection Parameter-average_value","Item Quality Inspection Parameter-test_standard","Item Quality Inspection Parameter-units","Quality Inspection Parameter-standard","Work Order Item-qty_by_volume","Work Order Item-specific_gravity","Work Order Item-percentage","Stock Entry-process_loss","Stock Entry-total_input_qty","Stock Entry-total_output_qty","BOM Item-specific_gravity","Stock Entry-is_process_bom","Work Order Item-qty_per_sub_batches","Work Order-sub_batches","Production Plan Item-item_category_custom","BOM-total_percentage","BOM-is_process_bom","Work Order Item-item_category_custom","Work Order-item_category_custom","BOM-item_category_custom","Item-item_category_custom","BOM Item-qty_by_volume","BOM Item-percentage","BOM-process_loss","BOM-material_parameters","BOM-quality_inspection_template_custom","Item-volume_solid_percent","Item-specific_gravity","Item-item_other_information","Item-item_alias_code","Item-column_break_30","Item-item_alias_name","Item-item_alias_section","Work Order-total_qty","Work Order-total_percentage","Work Order-table_of_specification","Work Order-specification","BOM-table_of_specification","BOM-section_break_59","BOM-machine","Work Order-party_name","Work Order-milling_hrs","BOM-procedure","BOM-milling_hrs","Work Order-machine","Work Order Item-item_group","Work Order Item-operation_custom","Work Order-procedure","Stock Entry Detail-carton_qty","Sales Invoice-boxes","Stock Entry Detail-label_description","Stock Entry Detail-label_name","Stock Entry Detail-carton_detail","Stock Entry Detail-carton_description","Sales Invoice-drums","Stock Entry Detail-item_description","Sales Invoice Item-additional_info","Sales Invoice Item-packing","Sales Order Item-additional_info","Quotation-gpap_header","Quotation-subject","Item-label_description","Item-hardener_qty","Item-base_qty","Item-column_break_57","Item-is_two_pack","Item-label_name","Item-labelling","Stock Entry-alias_qty","Stock Entry-alias_item","Item-parent_item","Item-is_alias","Item Price-mrp_rs","RND Project-workflow_state","RND Task-workflow_state","Item-bundle_uom","Item-bundle_size","Item-parent_item_group","Sales Order Item-customer_ref_code","Sales Invoice Item-customer_ref_code","Stock Entry Detail-auto_batch","Sales Invoice Item-manufacturing_date","Stock Entry Detail-mrp_custom","Stock Entry-disable_batch_logic","Item Quality Inspection Parameter-reading_value_custom","BOM-total_qty","Work Order-work_order_batch_reference","Quotation-blanket_order","Work Order-create_new_batch","Salary Slip-custom_present_days","Work Order Item-bundle_size","Work Order Item-bags","Work Order Item-loose"

            ]
        ]
    ]},
    {"dt": "Property Setter", "filters": [
        [
            "name", "in", ["Work Order-skip_transfer-default","Purchase Receipt-provisional_expense_account-hidden","Work Order-use_multi_level_bom-default","Quality Inspection-readings-allow_bulk_edit"
            ]
        ]
    ]},
	{"dt": "Letter Head", "filters": [
        [
            "name", "in", ["Work Order Letter Head"]
        ],
        [
            "name", "in", ["RP Work Order Letter Head"]
        ],
		[
            "name", "in", ["Goa Paints Logo"]
        ]
    ]},
	{"dt": "Stock Entry Type", "filters": [
        [
            "name", "in", ["Alias Transfer"]
        ]
    ]},
	{"dt": "Workflow", "filters": [
        [
            "name", "in", ["Workflow For RND Project"]
        ]
    ]},
]

# jenv = {
# 	"methods": ["get_print_scheme_data:goapaints_customization.goa_paints.jinja_function.get_paint_scheme_data.get_print_scheme_data"]
# }
jinja = {
	"methods": ["goapaints_customization.goa_paints.jinja_function.get_paint_scheme_data.get_print_scheme_data"]
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
# 		"goapaints_customization.tasks.all"
# 	],
# 	"daily": [
# 		"goapaints_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"goapaints_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"goapaints_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"goapaints_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "goapaints_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "goapaints_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "goapaints_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"goapaints_customization.auth.validate"
# ]

