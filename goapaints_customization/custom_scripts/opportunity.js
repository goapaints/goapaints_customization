frappe.ui.form.on('Opportunity', {
	refresh(frm) {
		if(!frm.is_new()){
            frm.add_custom_button(__('Paint Estimation Scheme'),function() {
                frappe.db.insert({
                    'doctype': 'Paint Estimation Scheme',
                    'customer': frm.doc.party_name,
                    'opportunity':frm.doc.name
                })
                frappe.msgprint("Your Paint Estimation Scheme is generated")
            }, __('Create'));
        }
	}
})