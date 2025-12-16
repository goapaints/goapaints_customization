frappe.ui.form.on('Production Plan', {
	refresh(frm) {
        // console.log("here")
		// frm.remove_custom_button('Work Order / Subcontract PO', 'Create');
        // if (frm.doc.docstatus === 1){
        //     if (frm.doc.po_items && frm.doc.status !== "Closed") {
        //         frm.add_custom_button(__("Work Order"), ()=> {
        //             frm.trigger("make_work_order_custom");
        //         }, __('Create'));
        //     }
        // }
	},
    // make_work_order_custom: function(frm) {
    //     // frappe.msgprint("Just a Test")
    //     // frm.trigger("make_work_order");
	// 	frappe.call({
	// 		'method': "goapaints_customization.goa_paints.custom_doctype.production_plan.production_plan.make_work_order_custom",
	// 		freeze: true,
    //         'args': {
    //             'doc': frm.doc,
    //         },
	// 		callback: function(res) {
	// 			// frm.reload_doc();
	// 		}
	// 	});
	// },
})