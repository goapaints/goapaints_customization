frappe.ui.form.on('BOM', {
	
	

	is_process_bom(frm){
	    if(frm.doc.is_process_bom === 1){
		    frm.set_value("quantity",100);
		    frm.refresh_field("quantity");
	}
		
		
	},
	quality_inspection_template_custom:function(frm){
	    if(frm.doc.quality_inspection_template_custom ){
    	        frappe.db.get_doc('Quality Inspection Template', null, {'quality_inspection_template_name':frm.doc.quality_inspection_template_custom})
                .then(doc => {
                
                cur_frm.clear_table("table_of_specification");
                
                for(var i in doc.item_quality_inspection_parameter){
                    var newrow = frappe.model.add_child(frm.doc, "Specification", "table_of_specification");
                    newrow.specification = doc.item_quality_inspection_parameter[i].specification;
                    newrow.status = doc.item_quality_inspection_parameter[i].status;
                    newrow.value = doc.item_quality_inspection_parameter[i].value;
                    newrow.numeric = doc.item_quality_inspection_parameter[i].numeric;
                    newrow.manual_inspection = doc.item_quality_inspection_parameter[i].manual_inspection;
                    newrow.min_value = doc.item_quality_inspection_parameter[i].min_value;
                    newrow.max_value = doc.item_quality_inspection_parameter[i].max_value;
                    newrow.formula_based_criteria = doc.item_quality_inspection_parameter[i].formula_based_criteria;
                    newrow.acceptance_formula = doc.item_quality_inspection_parameter[i].acceptance_formula;
                    newrow.units = doc.item_quality_inspection_parameter[i].units;
                    newrow.test_standard = doc.item_quality_inspection_parameter[i].test_standard;
                    newrow.is_process_parameter = doc.item_quality_inspection_parameter[i].is_process_parameter;
                    newrow.average_value = doc.item_quality_inspection_parameter[i].average_value;
                }
                cur_frm.refresh_fields("table_of_specification");
            });
	    }
	},
	validate(frm){
	    frm.doc.items.forEach((d) =>{
	        d.volume_solid_qty = (d.qty_by_volume*d.volume_solid_percent)/100;
	    });
        	    // var totalpercentage=0;
        	    var total_volume = 0;
        	    var total_kg = 0;
        	    var total_weight = 0;
        	    var total_volume_solid_qty = 0;
				var total_qty = 0;
        	    if(frm.doc.is_process_bom === 1){
            	        frm.doc.items.forEach(function(element){
                        total_volume += element.qty_by_volume;
                        total_volume_solid_qty += element.volume_solid_qty;
						total_qty += element.qty
                        
                    });
                    frm.set_value('total_volume',total_volume);
                    // frm.set_value('total_percentage',totalpercentage);
                    frm.set_value('density',total_qty/total_volume);
                    frm.set_value('total_weight',total_qty);
                    frm.set_value('total_volume_solid_qty',total_volume_solid_qty);
                    frm.set_value('volume_solid_percent',(frm.doc.total_volume_solid_qty/frm.doc.total_volume));
					frm.set_value('total_qty',total_qty);
                    // frm.refresh_field('total_percentage');
                    frm.refresh_field('total_volume');
                    frm.refresh_field('density');
                    frm.refresh_field('total_weight');
                    frm.refresh_field('total_volume_solid_qty');
                    frm.refresh_field('volume_solid_percent');
					frm.refresh_field('total_qty')
        	    }
                // if(frm.doc.is_process_bom === 1){
                //      if( totalpercentage != 100){
                //         frappe.throw("Total Percentage should be 100% ");
                        
                //     }
                // }else{
                //     frm.set_value('total_percentage',0);
                //     frm.refresh_field('total_percentage');
                // }
				if(frm.doc.is_process_bom === 1){
					if( total_qty != 100){
					   frappe.throw("Total Qty should be 100.00");
					   
				   }
			   }else{
				   frm.set_value('total_qty',0);
				   frm.refresh_field('total_qty');
			   }
                
	},
	// process_loss:function(frm,cdt,cdn){
	//     if(frm.doc.is_process_bom === 1){
    // 	        frm.doc.items.forEach((row)=>{
    // 	         row.qty = (row.percentage*(1+(frm.doc.process_loss/100)));
    // 	         row.qty_by_volume = row.qty/row.specific_gravity;
    // 	    });
	//     frm.refresh_field("items")
	//     }
	    
	// },

	
	

});

frappe.ui.form.on('BOM Item', {
	
	cal_qty:function(frm,cdt,cdn){
	    var row =locals[cdt][cdn];
	    if(frm.doc.is_process_bom === 1 && row.specific_gravity){
			console.log('here')
	        row.qty_by_volume = row.qty/row.specific_gravity;
	        row.volume_solid_qty = (row.qty_by_volume*row.volume_solid_percent)/100;
	        frm.refresh_field("items");
	    }
	},
	// percentage:function(frm,cdt,cdn){
	//     var row =locals[cdt][cdn];
	//     cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
	// },
	specific_gravity:function(frm,cdt,cdn){
	    var row =locals[cdt][cdn];
	    cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
	},
	qty:function(frm,cdt,cdn){
	    var row =locals[cdt][cdn];
	    cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
	}
});

frappe.ui.form.on('Specification', {
	
	is_process_parameter:function(frm,cdt,cdn){
	    var row = locals[cdt][cdn];
	        frappe.model.set_value(cdt,cdn,'average_value',(row.min_value+row.max_value)/2);
	    
	},
	min_value:function(frm,cdt,cdn){
	    var row = locals[cdt][cdn];
	        frappe.model.set_value(cdt,cdn,'average_value',(row.min_value+row.max_value)/2);
	},
	max_value:function(frm,cdt,cdn){
	    var row = locals[cdt][cdn];
	        frappe.model.set_value(cdt,cdn,'average_value',(row.min_value+row.max_value)/2);
	}
})