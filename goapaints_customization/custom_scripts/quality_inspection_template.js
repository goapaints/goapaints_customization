frappe.ui.form.on('Quality Inspection Template', {
	refresh(frm) {
		
	}
})

frappe.ui.form.on('Item Quality Inspection Parameter', {
	
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
});