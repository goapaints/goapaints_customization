frappe.ui.form.on('Quotation', {
	refresh(frm) {
        if(frm.doc.docstatus == 1){
            frm.add_custom_button(__('Blanket Order'),function() {
                if(frm.doc.blanket_order){
                    frappe.throw('Blanket Order for this document is already created!')
                }
                frappe.call({
                    method: 'goapaints_customization.goa_paints.custom_doctype.Quotation.quotation.make_blanket_order',
                    args: {
                        'self': frm.doc
                    },
                    callback: (r) => {
                        // on success
                    }
                })
            },__('Create'));
        }
	}
})

