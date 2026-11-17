# Copyright (c) 2022, Raj Tailor and contributors
# For license information, please see license.txt

# from ast import Continue
# from distutils.sysconfig import customize_compiler
import frappe
from frappe.model.document import Document
import json
import math
from functools import reduce

class PaintEstimationScheme(Document):
	pass

	def validate(self):
		for item in self.scheme_table:
			if item.dft != 0:
				item.tcc = ((item.vs/item.dft)*10)
			else:
				frappe.msgprint("Dft Value Cant Not Be Zero")
			item.pcc = (item.tcc * (1-(item.loss_factor/100)))
			# item.pcc_custom = (item.pcc /(item.touch_up_percentage/100))
			item.qty = int(item.area) / item.pcc
			if item.bundle_size != 0:
				round_qty = (math.floor(item.qty/item.bundle_size)+1)
				# frappe.msgprint(str(round_qty))
				item.rounded_qty = round_qty * item.bundle_size
			if round(item.qty) == item.bundle_size:
				item.rounded_qty = item.qty	

@frappe.whitelist()
def make_quotation(doc):
	try:
		doc = json.loads(doc)
		create_quot = frappe.new_doc('Quotation')
		create_quot.quotation_to = 'Customer'
		create_quot.party_name = doc["customer"]
		create_quot.transaction_date = doc["date"]
		create_quot.subject = doc["subject"]
		# create_quot.gpap_header = doc["gpap_header"]
		create_quot.tc_name = doc["tc_name"]
		create_quot.terms = doc["terms"]
		create_quot.opportunity = doc["opportunity"]
		grouped_items = group_by_item(doc["scheme_table"])
		for item in grouped_items:
			# group_by_item(doc["scheme_table"])
			# for item in doc["scheme_table"]:
			check_round_of = frappe.db.get_single_value("Goa Paints Custom Settings","round_of_qty")
			if check_round_of:
				qty = get_round_of_qty(item['bundle_size'],item['qty'])
			else:
				qty = item['qty']
			create_quot.append("items", {
				"item_code": item["item_code"],
				"qty": qty
			})
		create_quot.insert()
		create_quot_doc = create_quot.save()
		# frappe.msgprint(str(create_quot_doc.name))	
		frappe.msgprint('Your Quotation Is Created')
		frappe.db.set_value('Paint Estimation Scheme',doc["name"],'quotation',create_quot_doc.name)
		return create_quot_doc.name
	except Exception as e:
		frappe.msgprint("please fill all the field value for this document.")
		



def get_round_of_qty(bundle_size,qty):
	# for item in doc['scheme_table']:
	# 	frappe.msgprint(str(doc['scheme_table']))
	# frappe.msgprint(str(bundle_size))
	# frappe.msgprint(str(qty))
	if bundle_size != 0:
		round_qty = (math.floor(qty/bundle_size)+1)
		# frappe.msgprint(str(round_qty))
		qty_rounded =  round_qty*bundle_size
		# frappe.msgprint(str(qty_rounded))
	return qty_rounded

def group_by_item(items):
	
	data_list = []
	def reduce_data(result,data):
		key = data["item_code"]
		# key = ":".join([data["location"],data["surface_preparation"],data["area"]])
		data_to_add = {
			"qty":data["qty"]
			# All Data in one row
		}
		if key in result:
			result[key]['qty'] = result[key]['qty'] + data['qty']
			# add new row
		else:
			result[key]={
				'item_code':data['item_code'],
				'qty':data['qty'],
				'bundle_size':data['bundle_size']
			}
			# pass
			# Sum Qty Only, Keep all other data as it is
		return result
	data_list = reduce(reduce_data,items,{})
	# frappe.msgprint(str(data_list.values()))

	return list(data_list.values())	

# def sum_of_list_qty(item_list):
#	 item_qty_list = item_list['data_detail_list']
#	 frappe.throw(str(item_qty_list))

	
