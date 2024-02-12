import frappe
def get_context(context):
    context.ucenci = frappe.get_list("Ucenci", fields=["ucenec_id", "priimek", "qr_code"])
