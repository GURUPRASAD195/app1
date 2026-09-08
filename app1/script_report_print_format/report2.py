# Copyright (c) 2026, Guruprasad and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data()

    return columns, data


def get_columns():
    return [
        {
            "label": _("Name"),
            "fieldname": "name",
            "fieldtype": "Data",
        },
        {
            "label": _("Customer Name"),
            "fieldname": "customer_name",
            "fieldtype": "Data",
        },
        {
            "label": _("Phone Number"),
            "fieldname": "phone_number",
            "fieldtype": "Data",
        },
    ]


def get_data():
    return frappe.get_all(
        "Customers",
        fields=["name", "customer_name", "phone_number"]
    )