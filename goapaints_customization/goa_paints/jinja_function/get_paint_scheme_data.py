from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe.utils import flt,today
from frappe import _
import decimal    
import json
from datetime import datetime, timedelta
from functools import reduce





@frappe.whitelist()
def get_print_scheme_data(doc):
    estimate_doc = frappe.get_doc("Paint Estimation Scheme",doc.name)
    doc_scheme = get_grouped_data(estimate_doc.scheme_table)
    html = frappe.render_template("templates/print_estimation_scheme.html",{"doc":estimate_doc, "scheme": doc_scheme})
    return html


def get_grouped_data(data_of_dict):
    data_list = []
    def reduce_data(result,data):
        key = data.location
        # key = ":".join([data["location"],data["surface_preparation"],data["area"]])
        data_to_add = {
            "item_code": data.item_code,
            "item_name":data.item_name,
            "vs":data.vs,
            "dft":data.dft,
            "tcc":data.tcc,
            "loss_factor":data.loss_factor,
            "pcc":data.pcc,
            "touch_up_percentage":data.touch_up_percentage,
            "qty":data.qty,
            "rounded_qty":data.rounded_qty,
        }

        if key in result:
            result[key]["data_detail_list"].append(data_to_add)
        else:
            result[key] = {
            "location":data.location,
            "surface_preparation":data.surface_preparation,
            "area":data.area,
            "data_detail_list":[data_to_add]
            }
        return result
    data_list = reduce(reduce_data,data_of_dict,{})
    return list(data_list.values())
    
# print(get_grouped_data(temp_dict))