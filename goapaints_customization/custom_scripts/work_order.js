frappe.ui.form.on('Work Order', {
	refresh(frm) {
		
		frm.add_custom_button(__("Batch Qty Report"), ()=> {
            frappe.set_route("query-report","Batch-Wise Balance History", { "item_code": frm.doc.production_item });
        });
                        
        if(frm.doc.create_new_batch != 1 && !frm.is_new()){
            frm.add_custom_button(__("Create Batch"), ()=> {
                // frappe.msgprint("hello")
                let d = new frappe.ui.Dialog({
                    title: 'Create Item Batch',
                    
                    fields: [
                        {
                            label: 'Item Code',
                            fieldname: 'production_item',
                            fieldtype: 'Link',
                            options:'Item',
                            // default:frm.doc.production_item,
                            get_query: function () {
                                return {
                                    filters: {
                                        item_code: frm.doc.production_item
                                    },
                                    
                                };
                            },
                        },
                        {
                            label: 'Batch',
                            fieldname: 'batch',
                            // fieldtype: 'Link',
                            fieldtype: 'Data',
                            options: "Batch",
                            // get_query: function (row) {
                            //     return {
                            //         filters: {
                            //             item_code: frm.doc.production_item
                            //         },
                            //         query: 'erpnext.controllers.queries.get_batch_no'
                            //     };
                            // },
                        }
                    ],
                    primary_action_label: 'Create',
                    primary_action(values) {
                        console.log(values);
                        console.log(values.batch)
                        frappe.call({
                            method: "goapaints_customization.goa_paints.custom_doctype.Work_Order.work_order.create_batch",
                            args: {
                                'production_item': values.production_item                                ,
                                'batch': values.batch,
                                'doc':frm.doc.name,
                                'qty':frm.doc.qty
                            },
                            callback: function (r) {
                                console.log(r)
                                console.log(r.message)
                                frm.set_value("work_order_batch_reference",values.batch);
                                refresh_field("work_order_batch_reference");
                                
                                d.hide();
                            }
                        });
                        // d.hide();
                    }
                });
                // let dialog_items = d.fields_dict.production_item;
                // dialog_items.df.data.push({
                //     "production_item": frm.doc.production_item,
                // });
                // data = d.fields_dict.production_items.df.data;
                d.show();
                
            });
        }

        if(frm.doc.work_order_batch_reference){
            frm.remove_custom_button('Create Batch');
        }
        
        
        if(frappe.user_roles.includes("Manufacturing Manager") === true && frm.doc.docstatus == 1){
            frm.add_custom_button(__("Create RP Form"), ()=> {
                frappe.model.open_mapped_doc({
                    method: "goapaints_customization.goa_paints.custom_doctype.Work_Order.work_order.create_rp_from",
                    frm: cur_frm
                })
            });
		}
        
	},

    validate(frm){
        
        var total_qty = 0;
        var total_volume = 0;
        frm.doc.required_items.forEach(function(element){
            element.qty_per_sub_batches = element.required_qty/frm.doc.sub_batches;
            element.qty_by_volume = element.required_qty/element.specific_gravity
            total_qty += element.required_qty
            total_volume += element.qty_by_volume
            
        });
        console.log(total_volume)
        frm.set_value("total_qty",total_qty)
        frm.set_value("total_volume",total_volume)
        frm.refresh_field("total_qty","total_volume")

        frm.doc.required_items.forEach(function(item) {
            calculateCustomValues(frm, item.doctype, item.name);
        });
        
    }
});

frappe.ui.form.on('Work Order Item', {
	refresh(frm) {
		// your code here
	},
    cal_qty:function(frm,cdt,cdn){
        var row =locals[cdt][cdn];
        if(row.specific_gravity){
            row.qty_by_volume = row.required_qty/row.specific_gravity;
            frm.refresh_field("items");
        }
    },
    specific_gravity:function(frm,cdt,cdn){
        var row =locals[cdt][cdn];
        cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
    },
    required_qty:function(frm,cdt,cdn){
        var row =locals[cdt][cdn];
        cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
    },
    bundle_size: function(frm, cdt, cdn) {
        calculateCustomValues(frm, cdt, cdn);
    },
})


function calculateCustomValues(frm, cdt, cdn) {
    
    var child = locals[cdt][cdn];
    
    var bags = Math.floor(child.required_qty / child.bundle_size);
    var loose = child.required_qty - (child.bundle_size * bags);
    frappe.model.set_value(cdt, cdn, 'bags', bags);
    frappe.model.set_value(cdt, cdn, 'loose', loose);
    frm.refresh_field('custom_bags');
    frm.refresh_field('custom_loose');
    
    
}
