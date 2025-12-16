# Copyright (c) 2022, Raj Tailor and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RNDTask(Document):
	pass

	def validate(self):
		workflow_value = frappe.db.get_value('RND Project',{'name':self.rnd_project},'workflow_state')
		frappe.msgprint(str(workflow_value))
		if self.result ==  "Trial" and workflow_value == "Not Started":
			frappe.db.set_value('RND Project',{'name':self.rnd_project},'workflow_state','Under Development')
		if self.result in ["Approved","Rejected","Final"] and workflow_value == "Under Development":
			frappe.msgprint(str('hello'))
			frappe.db.set_value('RND Project',{'name':self.rnd_project},'workflow_state','Completed')