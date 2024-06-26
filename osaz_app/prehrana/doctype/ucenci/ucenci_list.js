frappe.listview_settings['Ucenci'] = {

    onload: function (listview) {

        // Add a button for doing something useful.
        listview.page.add_inner_button(__("Poišči QR"), function () {
            const scanner = new frappe.ui.Scanner({
                dialog: true, // open camera scanner in a dialog
                multiple: true, // stop after scanning one value
                on_scan(data) {
                    console.log(data.decodedText)
                    frappe.call('ping')
                        .then(r => {
                            console.log(r)
                            // {message: "pong"}
                        });
                    var data1 = data.decodedText;
                    frappe.db.get_value('Ucenci', { ucenec_id: data1 }, ['ime', 'priimek', 'oddelek', 'name'])
                        .then(r => {
                            let values = r.message;
                            console.log(values.ime);
                            console.log(values);
                            //frappe.set_route("ucenci/"+values.name)//#odpri en zapis

                            //frappe.msgprint({
                            //   title: __('Notification'),
                            //   indicator: 'green',
                            //  message: __(values.ime + values.priimek + values.oddelek)

                            //});
                            //show alert
                            frappe.show_alert({
                                message: __(values.ime + values.priimek + values.oddelek + values.name),
                                indicator: 'green'
                            }, 2);



                        });



                }
            });



            // change to your function's name
        })
            .addClass("btn-warning").css({ 'background': 'red', 'font-weight': 'normal', 'font-color': 'white' });
        //.addClass("btn-warning").css({'background':'darkred','font-weight': 'normal'});
        // The .addClass above is optional.  It just adds styles to the button.
    }
};