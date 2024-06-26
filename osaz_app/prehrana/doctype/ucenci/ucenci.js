// Copyright (c) 2023, osaz and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Ucenci", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Ucenci', {
	refresh: function (frm) {

	}
});

frappe.ui.form.on("Ucenci", "refresh", function (frm) {
	frm.add_custom_button(__("Do Something"), function () {
		// When this button is clicked, do this

		var subject = frm.doc.subject;
		var event_type = frm.doc.event_type;

		// do something with these values, like an ajax request 
		// or call a server side frappe function using frappe.call
		$.ajax({
			url: "http://example.com/just-do-it",
			data: {
				"subject": subject,
				"event_type": event_type
			}


			// read more about $.ajax syntax at http://api.jquery.com/jquery.ajax/

		});
	});
});

const scanner = new frappe.ui.Scanner({
	dialog: true, // open camera scanner in a dialog
	multiple: false, // stop after scanning one value
	on_scan(data) {


		console.log(data.decodedText)
		frappe.call('ping')
			.then(r => {
				console.log(r)
				// {message: "pong"}
			});
		var data1 = data.decodedText;
		frappe.db.get_value('Ucenci', { ucenec_id: data1 }, ['ime', 'priimek', 'oddelek'])
			.then(r => {
				let values = r.message;
				console.log(values.ime);
				frappe.msgprint({
					title: __('Notification'),
					indicator: 'green',
					message: __(values.ime)

				});

					});
				}
			})

		