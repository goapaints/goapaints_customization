frappe.ui.form.on('Sales Order', {
	refresh(frm) {
		// your code here
	},
	
})

frappe.ui.form.on('Sales Order Item', {
	refresh(frm) {
		// your code here
	},
	item_code: function(frm,cdt,cdn){
	    var row = locals[cdt][cdn];
	    frappe.db.get_doc('Item', row.item_code)
            .then(doc => {
                console.log(doc)
                console.log(doc.customer_code)
                row.customer_ref_code =  doc.customer_code;
                frappe.model_set_value(cdt,cdn,'customer_ref_code',doc.customer_code);
            });
	}
})