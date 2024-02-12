# Copyright (c) 2023, osaz and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Obrok(Document):
	#pass
	def validate(self):
		self.ucenec_link = "12345"