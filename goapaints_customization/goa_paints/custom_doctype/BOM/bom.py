import frappe

def validate(doc,method):
    for item in doc.items:
        if item.item_code == doc.item:
            frappe.throw("You can not add item itself in Material Required Table!")
def on_submit(doc,method):
    if doc.is_default == 1:
        frappe.db.set_value('BOM Item',{'item_code':doc.item},'bom_no',doc.name)