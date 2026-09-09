import frappe
from frappe.rate_limiter import rate_limit

@frappe.whitelist(allow_guest = True)
@rate_limit(limit=10, seconds=60)
def limited_greeting():
    logger = frappe.logger()
    logger.info("Endpoint called.")

    frappe.response['message'] = 'Hello, Rate Limited World!'