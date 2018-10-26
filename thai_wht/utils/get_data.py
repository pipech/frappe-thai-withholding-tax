import frappe
import datetime


def get_site_data(site_status):
    site_data = {}

    # prepare function list
    func_list = [
        get_last_active(),
    ]
    if site_status == 3:
        func_list.extend([
            get_total_whdee_whder(),
            get_total_doc(datetime.date.today()),
        ])

    # loop function list
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


def get_total_doc(today):
    # get last month and year
    last_day_previous_month = today - datetime.timedelta(days=today.day)
    month = last_day_previous_month.month
    year = last_day_previous_month.year

    # get pnd list
    pnd_list = frappe.get_all(
        doctype='Pnd',
        fields=['name'],
        filters={
            'month': month,
            'year': year,
            }
    )

    if pnd_list:
        # convert list of dict to name str with comma
        pnd_names = []
        for pnd in pnd_list:
            pnd_names.append('"{}"'.format(pnd['name']))
        pnd_name_where_sql = ', '.join(pnd_names)

        # get wht cert count from pnd list
        sql = """
        SELECT
            COUNT(*) AS 'wht_cert'
        FROM `tabPnd Detail`
        WHERE `parent` in ({where_sql});
        """.format(
            where_sql=pnd_name_where_sql
        )
        total_wht_cert = frappe.db.sql(sql, as_dict=1)[0]

        return {
            'total_doc': {
                'date': today.strftime('%Y-%m-%d'),
                'wht_cert': total_wht_cert['wht_cert'],
                'pnd': len(pnd_list)
            }
        }
