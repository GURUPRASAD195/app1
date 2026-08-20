let d = new frappe.ui.Dialog({
    title: "Create Task",

    fields: [
        {
            label: "Task Subject",
            fieldname: "task_subject",
            fieldtype: "Data",
            reqd: 1
        }
    ],

    primary_action_label: "Create Task",

    primary_action(values) {
        frappe.call({
            method: "app1.api.create_task",

            args: {
                task_subject: values.task_subject
            },

            callback: function(r) {
                d.hide();

                frappe.msgprint({
                    title: "Success",
                    message: "Task created successfully: " + r.message,
                    indicator: "green"
                });
            }
        });
    }
});

d.show();
