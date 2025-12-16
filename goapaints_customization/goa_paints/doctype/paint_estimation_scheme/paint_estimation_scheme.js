frappe.ui.form.on('Paint Estimation Scheme', {
	refresh(frm) {
		frm.set_query("item_code", "scheme_table", function(doc, cdt, cdn) {
    	var d = locals[cdt][cdn];
    	return{
    		filters: {
    			    'is_sales_item' : 1
    		    }
    	    }
        });
            frm.add_custom_button('Create Quotation', () => {
                if(frm.doc.quotation){
                    frappe.throw('Quotaion for this scheme is already created!');
                    }
                    else{
                        frappe.call({
            			'method': "goapaints_customization.goa_paints.doctype.paint_estimation_scheme.paint_estimation_scheme.make_quotation",
                        'args': {
                            'doc': frm.doc,
                        },
            			callback: function(res) {
            			    console.log(res);
            			    if(res.message){
            			        frm.set_value("quotation",res.message);
            			        refresh_field("quotaion");
            			    }
            			    frm.reload_doc();
            			}
		            });
                    
                    
                }
                
            });
        
    }
});

frappe.ui.form.on('Paint Estimation Scheme Table', {
	refresh(frm) {
		 //your code here
	},
	vs:function(frm,cdt,cdn){
	    var row = locals[cdt][cdn];
	    frappe.model.set_value(cdt,cdn,'tcc',(row.vs/row.dft)*10);
	},
	dft:function(frm,cdt,cdn){
	    var d = locals[cdt][cdn];
	    frappe.model.set_value(cdt,cdn,'tcc',(d.vs/d.dft)*10); 
		frappe.model.set_value(cdt,cdn,'pcc',d.tcc*(1-(d.loss_factor/100)));
	},
	loss_factor:function(frm,cdt,cdn){
	    var c = locals[cdt][cdn];
	    frappe.model.set_value(cdt,cdn,'pcc',c.tcc*(1-(c.loss_factor/100)));
	},
	touch_up_percentage:function(frm,cdt,cdn){
	    var l = locals[cdt][cdn];
	    // frappe.model.set_value(cdt,cdn,'qty',(l.area/l.pcc));
		frappe.model.set_value(cdt,cdn,'qty',(l.area/l.pcc)*(l.touch_up_percentage/100));
	},
	area:function(frm,cdt,cdn){
	    var m = locals[cdt][cdn];
	    // frappe.model.set_value(cdt,cdn,'qty',(m.aream/m.pcc));
		frappe.model.set_value(cdt,cdn,'qty',(m.area/m.pcc)*(m.touch_up_percentage/100));
	},
	
    

	
})