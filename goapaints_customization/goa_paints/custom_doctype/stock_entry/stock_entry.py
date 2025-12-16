import frappe
from frappe.utils import today

def validate(doc,method):

    type_list = ["Manufacture", "Repack","Alias Transfer"]

    if doc.stock_entry_type in type_list:
        custom_doc = frappe.get_doc('Goa Paints Custom Settings')

        if custom_doc.is_enabled_mrp_pricing == 1:
            mrp_price_list = custom_doc.mrp_price_list

            for item in doc.items:
                if item.is_finished_item:
                    mrp_item_price = frappe.db.get_value("Item Price",{'item_code': item.item_code, 'price_list': mrp_price_list},'price_list_rate') or 0

                    if item.mrp_custom == 0:
                        item.mrp_custom = mrp_item_price



    if not doc.is_process_bom:
        sfg_batch = ""
        fg_item = frappe.db.get_value("BOM",doc.bom_no,"item")
        if fg_item:
            sfg = frappe.db.get_value("Item",fg_item,"sfg_item_reference")
            if sfg:
                for item in doc.items:
                    if item.item_code == sfg:
                        # frappe.msgprint(str(item.item_code))
                        sfg_batch = item.batch_no
        doc.sfg_batch_no = sfg_batch
    # if not doc.disable_batch_logic:
    #     for item in doc.items:
    #         get_data = frappe.db.get_value('Item',{'item_code':item.item_code},'item_category_custom')
    #         get_bundle = frappe.db.get_value('Item',{'item_code':item.item_code},'bundle_size')
    #         fg_batch = str(sfg_batch)+"/"+str(get_bundle)
    #         if get_data == 'Finished Goods' and item.is_finished_item == 1 and not item.auto_batch:
    #             if not frappe.db.exists("Batch",fg_batch):
    #                 create_batch = frappe.get_doc({
    #                     'doctype':'Batch',
    #                     # 'batch_id' : "FG-"+str(get_bundle)+"-"+str(sfg_batch),
    #                     'batch_id' :fg_batch,
    #                     'item' : item.item_code,
    #                     'item_name' : item.item_name,
    #                     'manufacturing_date' : frappe.utils.nowdate(),
    #                     'stock_uom' : item.stock_uom
    #                 })
    #                 create_batch.save()
    #                 frappe.msgprint("Auto FG Batch Created "+str(create_batch))
    #                 # item.batch_no = "FG-"+str(get_bundle)+"-"+str(sfg_batch)
    #             item.batch_no = fg_batch

def create_fg_batch(sfg_batch,bundle_size):
    return 

@frappe.whitelist()
def make_quality_inspection_custom(doc):
    self = frappe.get_doc('Stock Entry', doc)
    work_order = frappe.get_doc('Work Order', self.work_order)

    item = []
    item = [i for i in self.items if i.is_finished_item == 1]

    qi = frappe.new_doc('Quality Inspection')
    qi.report_date = today()
    qi.status = "Accepted"
    qi.inspection_type = "Incoming"
    qi.reference_type = "Stock Entry"
    qi.reference_name = self.name
    qi.item_code = item[0].item_code
    qi.item_name = item[0].item_name
    qi.batch_no = item[0].batch_no
    qi.description = item[0].description
    qi.sample_size = 0
    qi.inspected_by = frappe.session.user
    for i in work_order.table_of_specification:
        row = qi.append('readings', {})
        row.specification = i.specification
        row.value = i.value
        row.status = i.status
        row.min_value = i.min_value
        row.max_value = i.max_value
        row.average_value_ = i.average_value
        row.numeric = i.numeric
        row.test_standard = i.test_standard
        row.units = i.units
        row.manual_inspection = i.manual_inspection
        row.formula_based_criteria = i.formula_based_criteria

    qi.save(ignore_permissions = True)

    # frappe.msgprint('Quality Inspection Created Successfully!')
    return qi.name
