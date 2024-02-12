import frappe
from datetime import date


def get_context(context):
    context.devices = frappe.get_all("Device",fields=["name"]) # type: ignore
    context.events = frappe.get_all("Event",fields=["name", "starts_on", "ends_on", "subject"])
    context.notes = frappe.get_all("Note",fields=["name", "title", "content", "public"])



