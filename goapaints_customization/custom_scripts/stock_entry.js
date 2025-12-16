frappe.ui.form.on('Stock Entry', {
    setup: function(frm) {
	        frm.set_query("alias_item", function() {
	           return {
    				filters: [
    					["Item","is_alias","=",1]
    				]
			};
		});
	},
    alias_qty:function(frm){
	    if (frm.doc.alias_item && frm.doc.alias_qty){
	           
	            frappe.db.get_value('Item', {'is_alias':1,'item_code':frm.doc.alias_item}, ['parent_item', 'stock_uom','item_name'])
                    .then(r => {
                        let values = r.message;
                        console.log(values.parent_item, values.stock_uom,values.item_name);
                        frm.set_value("items",[])
                        let row = frm.add_child('items', {
                            item_code: frm.doc.alias_item,
                            item_name:values.item_name,
                            qty: frm.doc.alias_qty,
                            stock_uom:values.stock_uom,
                            uom:values.stock_uom,
                            conversion_factor:1,
                            transfer_qty:frm.doc.alias_qty
                        });
                        frm.refresh_field('items');
                        let child_row = frm.add_child('items', {
                            item_code:values.parent_item ,
                            item_name:values.item_name,
                            qty: frm.doc.alias_qty,
                            stock_uom:values.stock_uom,
                            uom:values.stock_uom,
                            conversion_factor:1,
                            transfer_qty:frm.doc.alias_qty
                        });
                        frm.refresh_field('items');
                    });
	    }
	    
	},
	refresh(frm) {
        frm.remove_custom_button('Quality Inspection(s)', 'Create');
        console.log(frm.doc)
        if (frm.doc.docstatus === 0){
            if (frm.doc.inspection_required === 1 && !frm.doc.quality_inspection_custom) {
                frm.add_custom_button(__("Quality Inspection Custom"), ()=> {
                    frm.trigger("make_quality_inspection_custom");
                }, __('Create'));
            }
        }
	},
    make_quality_inspection_custom: function(frm) {
        // frappe.msgprint("Just a Test")
        // frm.trigger("make_work_order");
        if(!frm.doc.quality_inspection_custom){
            frappe.call({
                'method': "goapaints_customization.goa_paints.custom_doctype.stock_entry.stock_entry.make_quality_inspection_custom",
                freeze: true,
                'args': {
                    'doc': frm.doc.name,
                },
                callback: function(res) {
                    // frm.reload_doc();
                    console.log(res)
                    if(res.message){
                        frm.set_value("quality_inspection_custom",res.message)
                        frm.refresh_field("quality_inspection_custom")
                        frappe.msgprint("qulaity inspection template is created!")
                        frm.save()
                    }
                    
                }
            });
        }
		
	},
	specific_gravity(frm){
	  if(frm.doc.is_process_bom === 1 && frm.doc.specific_gravity){
	      frm.set_value('output_litre',frm.doc.total_output_qty/frm.doc.specific_gravity);
	  }  
	},
	validate(frm){
	    var total_input_qty = 0;
	    var total_output_qty = 0;
	    frm.doc.items.forEach((row)=>{
	            if(row.s_warehouse){
	               // row.total_input_qty = row.qty;
	                total_input_qty += row.qty;
	                
	            } 
	            else if(row.t_warehouse){
	               // row.total_output_qty = row.qty;
	                    total_output_qty += row.qty;
	  
	            }
	           // row.process_loss = frm.doc.fg_completed_qty - row.total_input_qty - row.total_output_qty;
	    }); 
	            frm.set_value("total_input_qty",total_input_qty);
                frm.refresh_field("total_input_qty");
                frm.set_value("total_output_qty",total_output_qty);
                frm.refresh_field("total_output_qty");
                frm.set_value("process_loss",total_input_qty-total_output_qty);
                frm.refresh_field("process_loss");
                frm.set_value("process_loss_perc",frm.doc.process_loss/frm.doc.total_input_qty);
                frm.refresh_field("process_loss_perc");
        if(frm.doc.is_process_bom){
	    frm.set_value("inspection_required",1)
	    frm.refresh_field("inspection_required")
	}
                
	}
})
