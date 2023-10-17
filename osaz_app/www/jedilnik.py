import frappe
from datetime import date


def get_context(context):
    context.jedilnik = frappe.get_all("Jedilnik",fields=["datum", "zajtrk", "malica", "kosilo"]) # type: ignore



