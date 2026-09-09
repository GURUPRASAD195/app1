import frappe

def get_context(context):
    context.articles = frappe.get_all(
        "articles", 
        filters={"published" : 1},
        fields=["title", "name"])