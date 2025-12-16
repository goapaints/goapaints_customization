frappe.ui.form.on('Item', {
	refresh(frm) {
		// your code here
	},
	setup: function(frm) {
	        frm.set_query("sfg_item_reference", function() {
			return {
				filters: [
					["Item","item_category_custom","in",["Semi Finished Goods"]]
				]
			};
		});
	},
	base_qty(frm){
	    frm.set_value('hardener_qty',frm.doc.bundle_size-frm.doc.base_qty);
	    frm.refresh_field('hardener_qty');
	}
})