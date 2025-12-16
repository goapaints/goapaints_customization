frappe.ui.form.on('RND Project', {
	refresh(frm) {
			frm.add_custom_button(__("Create RND Task"), ()=> {
                    // frappe.set_route("form","RND Task", frm.doc.name);
                    create_doc = frappe.new_doc('RND Task');
                    create_doc.machine = 'Ball Mill';
                    
                });
	},
	setup: function(frm) {
	        frm.set_query("product", function() {
	            if(frm.doc.task_type == "Raw Material"){
	                return {
				filters: [
					["Item","allow_purchase","=",1]
				]
			};
	            }
			
		});
	}
});
