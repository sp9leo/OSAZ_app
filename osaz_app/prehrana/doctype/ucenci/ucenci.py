# Copyright (c) 2023, osaz and contributors
# For license information, please see license.txt

#import frappe
from frappe.model.document import Document
from frappe.utils import get_abbr, random_string

from osaz_app.qr_code import get_qr_code

#class Ucenci(Document):
#	pass

class Ucenci(Document):
	def validate(self):
		a=str(self.zajtrk).replace("1","Z")
		b=str(self.malica).replace("1","M")
		c=str(self.kosilo).replace("1","K")
		d=str(self.vozac).replace("1","V")
		e=str(self.dieta).replace("1","D")
		n=str(self.name)
		o=str(self.oddelek)
		#name = random_string(12)+"000"+ a + b + c + d +e
		name = n+"000"+ a + b + c + d +e
		name = str(name)
		qrcode = str(n+"0"+o)
		self.ucenec_id = name
		self.qr_code = get_qr_code(qrcode)
		#self.qr_code = get_qr_code(self.ucenec_id)
		#self.ucenec_id = get_qr_code(self.<field>)

		

		