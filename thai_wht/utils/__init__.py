import frappe


def add_system_manager(email, pwd):
    from frappe.utils.password import update_password
    from frappe.utils.user import add_system_manager
    add_system_manager(email=email)
    update_password(user=email, pwd=pwd)


def disable_signup():
    disable_signup_sql = """
        UPDATE `tabSingles`
        SET
            `value`='1'
        WHERE
            `doctype`='Website Settings'
            AND
            `field`='disable_signup'
        ;"""
    frappe.db.sql(disable_signup_sql, auto_commit=1)
