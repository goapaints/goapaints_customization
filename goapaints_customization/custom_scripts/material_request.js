frappe.ui.form.on('Material Request', {
	refresh(frm) {
		// console.log("here")
		frm.remove_custom_button('Work Order', 'Create');
	},
	onload:function(frm){
        frm.remove_custom_button('Work Order', 'Create');
    }
})