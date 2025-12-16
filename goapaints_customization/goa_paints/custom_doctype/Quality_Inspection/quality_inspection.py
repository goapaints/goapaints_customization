import frappe

def validate(doc,method):
    pass
    # if doc.batch_no:
    #     batch = frappe.db.get_value('Batch',{'item':doc.item_code,'reference_doctype':'Work Order'},'reference_name')
    #     # frappe.msgprint(str(batch))
    #     # work_order = frappe.db.get_value('Work Order',{'name':batch},'production_plan')
    #     # frappe.msgprint(str(work_order))
    #     # frappe.db.set_value('Production Plan', {'name':work_order}, 'sfg_quality_inspection', doc.name)
