# import frappe

# def custom_logic(doc, method):
#     frappe.msgprint("Hook executed!")


import frappe


@frappe.whitelist()
def student_course_report():
    Student = frappe.qb.DocType("Student1")
    Course = frappe.qb.DocType("Course")

    query = (
        frappe.qb.from_(Student)
        .inner_join(Course)
        .on(Student.course == Course.name)
        .select(
            Student.name,
            Student.student_name,
            Student.course,
            Course.department
        )
    )
    results = query.run(as_dict=True)

    if results:
        doc = frappe.get_doc("Student1", results[0]["name"])

        doc.student_name = doc.student_name + " Updated"

        doc.save()

    for row in results:
        frappe.db.set_value(
            "Student1",
            row["name"],
            "status",
            "Processed"
        )

    return results


import frappe

frappe.utils.logger.set_log_level("DEBUG")

logger = frappe.logger("student", allow_site=True)

@frappe.whitelist(allow_guest=True)
def test_logging():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

    return "Logging test completed"


import frappe


@frappe.whitelist()
def get_latest_pyapi5():

    records = frappe.get_list(
        "pyapi5",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit_page_length=5
    )

    result = []

    for record in records:

        email = frappe.db.get_value(
            "User",
            record.owner,
            "email"
        )

        result.append({
            "name": record.name,
            "description": record.description,
            "owner_email": email
        })

    return {
        "timestamp": frappe.utils.now(),
        "records": result
    }