import frappe
from frappe.utils import today
from frappe.model.mapper import get_mapped_doc

def validate(doc,method):
    # last_batch = frappe.db.sql(""" select name from `tabBatch` where item = %s order by creation desc limit 1""",doc.production_item)
    last_batch = frappe.db.sql(""" select name from `tabBatch` where item = %s and reference_name != %s order by creation desc limit 1""",(doc.production_item,doc.name))

    if last_batch:
        doc.last_batch = last_batch[0][0]
    if doc.production_item:
        tab = frappe.get_doc('BOM', doc.bom_no)
        doc.set('table_of_specification',[])
        for item in tab.table_of_specification:
                doc.append('table_of_specification',{
                    'specification':item.specification,
                    'staus':item.status,
                    'value':item.value,
                    'numeric':item.numeric,
                    'manual_inspection':item.manual_inspection,
                    'min_value':item.min_value,
                    'max_value':item.max_value,
                    'formula_based_criteria':item.formula_based_criteria,
                    'acceptance_formula':item.acceptance_formula,
                    'units':item.units,
                    'test_standard':item.test_standard,
                    'is_process_parameter':item.is_process_parameter,
                    'average_value':item.average_value
                })

    # if doc.is_process_bom:    
    #     totalqty=0
    #     total_vol = 0
    #     total_weight = 0
    #     for item in doc.required_items:
    #         values_from_bom_item = frappe.db.get_value("BOM Item",{"parent":doc.bom_no,"item_code":item.item_code},["percentage"])
    #         if values_from_bom_item:
    #             item.percentage = values_from_bom_item
    #             item.qty_by_volume = float(item.required_qty)/float(item.specific_gravity)
    #             totalqty = totalqty + item.required_qty
    #             total_vol = total_vol + item.qty_by_volume
    #             total_weight = total_weight + item.required_qty
    #     doc.total_qty = totalqty
    #     doc.total_volume = total_vol
    #     doc.density = totalqty/total_vol if total_vol else 0
    #     doc.total_weight = total_weight


@frappe.whitelist()
def create_batch(batch,production_item,doc,qty):
     batch_doc = frappe.new_doc("Batch")
     batch_doc.batch_id = batch
     batch_doc.item = production_item
     batch_doc.item_name = frappe.db.get_value("Item",production_item,'item_name')
     batch_doc.manufacturing_date = today()
     batch_doc.reference_doctype = "Work Order"
     batch_doc.reference_name = doc
     batch_doc.qty_to_produce = qty
     batch_doc.insert()
    
     frappe.msgprint("For This <b>{}</b> Item Batch is <b>{}</b> created".format(production_item,batch))

@frappe.whitelist()
def create_rp_from(source_name, target_doc=None):
     doclist = get_mapped_doc(
        "Work Order",
		source_name, 
		{
			"Work Order": {
				"doctype": "RP Work Order",
				"field_map": {
					"status": "status",
					"production_item": "production_item",
                     "name":"work_order_reference"    
				},
				# "field_no_map": ["payment_terms_template"],
				# "validation": {"docstatus": ["=", 1]},
			},
			"Work Order Item": {
				"doctype": "Work Order Item",
				"field_map": {
					"item_code": "item_code",
					"item_name": "item_name",
				},
				
			},
			# "Sales Taxes and Charges": {"doctype": "Sales Taxes and Charges", "add_if_empty": True},
			# "Sales Team": {"doctype": "Sales Team", "add_if_empty": True},
		},
		# target_doc,
		# postprocess,
		# ignore_permissions=ignore_permissions,
        target_doc
	) 
     return doclist    