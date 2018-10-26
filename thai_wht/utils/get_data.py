import frappe


def get_site_data():
    site_data = {}

    func_list = [
        get_last_active(),
        get_total_whdee_whder(),
    ]

    for func in func_list:
        func_return = func
        if func_return:
            site_data.update(func_return)

    return site_data


def get_last_active():
    sql = 'SELECT MAX(`last_active`) AS last_active FROM `tabUser`;'
    last_active = frappe.db.sql(sql, as_dict=1)
    last_active = last_active[0].get('last_active')
    if last_active:
        last_active = last_active.strftime('%Y-%m-%d %H:%M:%S')
        return {'last_active': last_active}


def get_total_whdee_whder():
    sql = """
    SELECT
        (SELECT COUNT(*) FROM tabWhdee) AS 'whdee',
        (SELECT COUNT(*) FROM tabWhder) AS 'whder'
        """
    total_whdee_whder = frappe.db.sql(sql, as_dict=1)[0]
    return total_whdee_whder
