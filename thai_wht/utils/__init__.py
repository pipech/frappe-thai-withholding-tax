import frappe


def add_system_manager(email, pwd):
    from frappe.utils.password import update_password
    from frappe.utils.user import add_system_manager
    add_system_manager(email=email)
    update_password(user=email, pwd=pwd)
