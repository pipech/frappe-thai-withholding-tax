import frappe


def get_site_data():
    site_data = {}

    data_list = [
        {
            'label': 'last_active',
            'func': get_last_active(),
        }
    ]

    for data in data_list:
        func_return = data['func']
        if func_return:
            site_data[data['label']] = func_return

    return site_data


def get_last_active():
    sql = 'SELECT MAX(`last_active`) AS last_active FROM `tabUser`;'
    last_active = frappe.db.sql(sql, as_dict=1)
    last_active = last_active[0].get('last_active')
    if last_active:
        last_active = last_active.strftime('%Y-%m-%d %H:%M:%S')
        return last_active
