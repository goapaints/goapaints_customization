import frappe

def validate(self,method):
    uoms_list = [d.uom for d in self.uoms]
    if self.bundle_size and self.bundle_uom not in uoms_list:
        self.append('uoms', {
            'uom':self.bundle_uom,
            'conversion_factor':self.bundle_size 
        })

    # if self.bundle_size and self.bundle_uom:
    #     self.append('uoms', {
    #             'uom':self.bundle_uom,
    #             'conversion_factor':self.bundle_size 
    #     })