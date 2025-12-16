import frappe
import json
from frappe import _, msgprint
from frappe.utils import (
	comma_and,
	get_link_to_form,
)

def before_insert(self, method):
    pass
#     if len(self.sub_assembly_items)>0:
#        assem_item = []
 
#        for item in self.sub_assembly_items:
#            if not assem_item:
#                item.item_category_custom = frappe.db.get_value('Item', item.production_item, 'item_category_custom')
#                assem_item.append(item)
#            else:
#                flag = False
#                for i in assem_item:
#                    if i.production_item == item.production_item:
#                        flag = True
#                        i.qty = i.qty + item.qty
              
#                if flag == False:
#                    item.item_category_custom = frappe.db.get_value('Item', item.production_item, 'item_category_custom')
#                    assem_item.append(item)
 
#        self.sub_assembly_items.clear()
#        self.sub_assembly_items = assem_item
 
#        for idx, row in enumerate(self.sub_assembly_items, start=1):
#            row.idx = idx
 
#        for item in self.po_items:
#            item.item_category_custom = frappe.db.get_value('Item', item.item_code, 'item_category_custom')

# @frappe.whitelist()
# def make_work_order_custom(doc):
#     from erpnext.manufacturing.doctype.work_order.work_order import get_default_warehouse

#     wo_list = []
#     default_warehouses = get_default_warehouse()

#     doc = json.loads(doc)
#     self = frappe.get_doc('Production Plan', doc['name'])
#     # frappe.msgprint(self.company)

#     make_work_order_for_finished_goods(self, wo_list, default_warehouses)
#     make_work_order_for_subassembly_items(self, wo_list, default_warehouses)
#     show_list_created_message('Work Order', wo_list)


# def make_work_order_for_finished_goods(self, wo_list, default_warehouses):
#     items_data = self.get_production_items()

#     for key, item in items_data.items():
#         if self.sub_assembly_items:
#             item['use_multi_level_bom'] = 0

#         set_default_warehouses(item, default_warehouses)
#         work_order = create_work_order(self, item)
#         if work_order:
#             wo_list.append(work_order)

# def make_work_order_for_subassembly_items(self, wo_list, default_warehouses):
#     for row in self.sub_assembly_items:

#         if row.item_category_custom != "Semi Finished Goods" and row.item_category_custom != "Intermediates - ToMake":
#             continue

#         work_order_data = {
#             'wip_warehouse': default_warehouses.get('wip_warehouse'),
#             'fg_warehouse': default_warehouses.get('fg_warehouse')
#         }

#         prepare_data_for_sub_assembly_items(self, row, work_order_data)
#         work_order = create_work_order(self, work_order_data)
#         if work_order:
#             wo_list.append(work_order)

# def show_list_created_message(doctype, doc_list=None):
#     if not doc_list:
#         return

#     frappe.flags.mute_messages = False
#     if doc_list:
#         doc_list = [get_link_to_form(doctype, p) for p in doc_list]
#         msgprint(_("{0} created").format(comma_and(doc_list)))

# def prepare_data_for_sub_assembly_items(self, row, wo_data):
#     for field in ["production_item", "item_name", "qty", "fg_warehouse",
#         "description", "bom_no", "stock_uom", "bom_level", "schedule_date"]:
#         if row.get(field):
#             wo_data[field] = row.get(field)

#     wo_data.update({
#         "use_multi_level_bom": 0,
#         "production_plan": self.name,
#         "production_plan_sub_assembly_item": row.name
#     })

# def set_default_warehouses(row, default_warehouses):
# 	for field in ['wip_warehouse', 'fg_warehouse']:
# 		if not row.get(field):
# 			row[field] = default_warehouses.get(field)
    

# def create_work_order(self, item):
#     from erpnext.manufacturing.doctype.work_order.work_order import OverProductionError

#     wo = frappe.new_doc("Work Order")
#     wo.update(item)
#     wo.planned_start_date = item.get("planned_start_date") or item.get("schedule_date")

#     if item.get("warehouse"):
#         wo.fg_warehouse = item.get("warehouse")

#     wo.set_work_order_operations()
#     wo.set_required_items()

#     bom = frappe.get_doc('BOM', wo.bom_no)
#     if bom.table_of_specification: 
#         for i in bom.table_of_specification:
#             row = wo.append('table_of_specification', {})
#             row.specification = i.specification
#             row.status = i.status
#             row.min_value = i.min_value
#             row.max_value = i.max_value
#             row.numeric = i.numeric
#             row.manual_inspection = i.manual_inspection
#             row.formula_based_criteria = i.formula_based_criteria

#     try:
#         wo.flags.ignore_mandatory = True
#         wo.flags.ignore_validate = True
#         wo.insert()
#         return wo.name
#     except OverProductionError:
#         pass