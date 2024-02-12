import frappe
from datetime import date


def get_context(context):
    context.jedilnik = frappe.get_all("Jedilnik",fields=['*']) # type: ignore
    context.zivila = frappe.get_all("Zivila Link",fields=["zivila_link", "parent", "parentfield"]) # type: ignore
    context.link= frappe.db.get_list('Zivila Link',
                    filters={
                        'parent': '30e33422af'
                    },
                    fields=['name', 'parent'],
                    
                    start=10,
                    page_length=20,
                    as_list=True)
    
    context.sql = frappe.db.sql("""
SELECT zivila_link, datum, parentfield FROM `tabZivila Link` AS zivila, tabJedilnik AS jedilnik
WHERE parent = jedilnik.name AND jedilnik.datum = '2024-01-23'
""")
    context.list= frappe.db.get_list('Zivila Link',
    fields=['parent', 'zivila_link'],
   
)





