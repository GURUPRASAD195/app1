import frappe


def daily_maintenance():
    frappe.log_error(
        "Daily maintenance job executed successfully",
        "Daily Maintenance"
    )

