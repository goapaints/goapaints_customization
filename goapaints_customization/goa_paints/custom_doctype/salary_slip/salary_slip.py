import frappe

def after_insert(self,method):
    attendance_days_count(self)

def validate(self,method):
    attendance_days_count(self)

def attendance_days_count(self):
    present_days_count = frappe.db.count("Attendance", {
        "employee": self.employee,
        "status": "Present",
        "docstatus": 1,
        "attendance_date": ["between", [self.start_date, self.end_date]]
    })
    if present_days_count:
        self.custom_present_days = present_days_count
    
    frappe.db.commit()
