import frappe
import json


def validate(self,method):
    if self.opportunity:
        frappe.db.set_value("Opportunity",self.opportunity,'status','Quotation')
def on_trash(self,method):
    frappe.db.set_value('Paint Estimation Scheme',{'quotation':self.name},'quotation','')


@frappe.whitelist()
def make_blanket_order(self):
    self = json.loads(self)
    bl_order = frappe.new_doc('Blanket Order')
    bl_order.customer = self["customer_name"]
    bl_order.customer_name = self['customer_name']
    bl_order.blanket_order_type = "Selling"
    bl_order.from_date = self['transaction_date']
    bl_order.to_date = self['transaction_date']
    items = self['items']
    for item in items:
        bl_order.append("items", {
			"item_code": item["item_code"],
			"qty": item["qty"],
            "rate":item["rate"]
		})
    bl_order.tc_name = self["tc_name"]
    bl_order.terms = self["terms"]    

    bl_order.insert()
    bl_order_doc = bl_order.save()
    frappe.db.set_value("Quotation",self['name'],'blanket_order',bl_order_doc.name)
    frappe.msgprint("Your Blanket Order is Created")