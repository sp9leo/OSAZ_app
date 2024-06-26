import frappe
from frappe.desk.doctype.event.event import get_events
from frappe.utils import add_to_date, nowdate
from datetime import datetime

#danes = datetime.datetime.now()
danes = frappe.utils.formatdate(frappe.utils.today(), 'dd-MM-YYYY')
#danes = today()
#zdaj = frappe.utils.today()
future_start = add_to_date(datetime.now(), days=1)
future_end = add_to_date(datetime.now(), days=14)


print (danes)

def get_todays_events(as_list=False):
	"""Returns a count of todays events in calendar"""
	today = nowdate()
	events = get_events(today, today)
	return events if as_list else len(events)

def get_future_events(as_list=False):
	"""Returns a count of todays events in calendar"""
	future_start = add_days(nowdate(),1)
	future_end = add_days(nowdate(),14)
	future_events = get_events(future_start,future_end)
	
	return future_events if as_list else len(future_events)


def get_context(context):
	
	
	
	context.test = future_end
	#context.future_events = get_future_events(as_list=True)
	context.future_events = frappe.get_all("Dogodek", filters={"published": 1, "event_type":"Public", "starts_on":[ ">", future_start, "<",future_end]}, fields=["name", "starts_on", "ends_on", "subject", "route", "color", "all_day", "event_type", "event_category", "location" ],order_by="starts_on asc")
	#context.events_today = get_todays_events(as_list=True) #events za na stran
	context.events_today = frappe.get_all("Dogodek", filters={"published": 1, "event_type":"Public", "starts_on":[ "between", danes, danes]}, fields=["name", "starts_on", "ends_on", "subject", "route", "color", "all_day", "event_type", "location","event_category"],order_by="starts_on asc") #events za na stran
	#context.events = get_todays_events(as_list=True) #events za koledar

	context.devices = frappe.get_all("Device",fields=["name"])
		# type: ignore
	#context.events_today = frappe.get_all("Event",filters={"published": 1},fields=["name", "starts_on", "ends_on", "subject", "route", "color", "all_day" ])
	context.calendar_events = frappe.get_all("Dogodek",filters={"published": 1, "event_type":"Public"},fields=["name", "starts_on", "ends_on", "subject", "route", "color", "all_day", "event_type", "event_category" ])
	context.obvestila = frappe.get_all("Obvestila",filters={"important": 0, "public":1, "zacetek":[ "between", danes, danes] },fields=["name", "title", "content", "public", "creation","important", "modified", "zacetek"], order_by="creation asc")
	context.important = frappe.get_list("Obvestila",filters={"important": 1, "public":1, "zacetek":[ "between", danes, danes]},fields=["name", "title", "content", "public", "modified","important", "zacetek"], order_by="modified desc")
	



