frappe.ui.form.on('RND Task', {
	refresh(frm) {
		// your code here
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
	    frm.doc.bom_items.forEach((d) =>{
	        d.volume_solid_qty = (d.qty_by_volume*d.volume_solid_percent)/100;
	    });
        	    // var totalpercentage=0;
        	    var total_volume = 0;
        	    var total_kg = 0;
        	    var total_weight = 0;
        	    var total_volume_solid_qty = 0;
    	        frm.doc.bom_items.forEach(function(element){
                    totalpercentage += element.percentage;
                    total_volume += element.qty_by_volume;
                    total_kg += element.qty;
                    total_weight += element.qty;
                    total_volume_solid_qty += element.volume_solid_qty;
                });
                    frm.set_value('total_volume',total_volume);
                    // frm.set_value('total_percentage',totalpercentage);
                    frm.set_value('density',total_kg/total_volume);
                    frm.set_value('total_weight',total_weight);
                    frm.set_value('total_volume_solid_qty',total_volume_solid_qty);
                    frm.set_value('volume_solid_percent',(frm.doc.total_volume_solid_qty/frm.doc.total_volume));
                    // frm.refresh_field('total_percentage');
                    frm.refresh_field('total_volume');
                    frm.refresh_field('density');
                    frm.refresh_field('total_weight');
                    frm.refresh_field('total_volume_solid_qty');
                    frm.refresh_field('volume_solid_percent');
                    
                     if( total_weight != 100){
                        frappe.throw("Total Qty should be 100% ");
                    }
                    // else{
                    //     frm.set_value('total_percentage',0);
                    //     frm.refresh_field('total_percentage');
                    // }
        
	   }
	           
})

frappe.ui.form.on('Table Of BOM Item', {
	refresh(frm) {
		// your code here
	},
	cal_qty:function(frm,cdt,cdn){
	    var row =locals[cdt][cdn];
	        // row.qty = (row.percentage*(1+(frm.doc.process_loss/100)));
	        row.qty_by_volume = row.qty/row.specific_gravity;
	        row.volume_solid_qty = (row.qty_by_volume*row.volume_solid_percent)/100;
	        frm.refresh_field("bom_items");
	},
	percentage:function(frm,cdt,cdn){
	    var row =locals[cdt][cdn];
	    cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
	},
	specific_gravity:function(frm,cdt,cdn){
	    var row =locals[cdt][cdn];
	    cur_frm.script_manager.trigger("cal_qty",cdt,cdn)
	}
})

frappe.ui.form.on('Specification', {
	refresh(frm) {
		// your code here
	},
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