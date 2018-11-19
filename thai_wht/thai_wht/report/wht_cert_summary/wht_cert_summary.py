# Copyright (c) 2013, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from frappe import _


def execute(filters=None):

    data = get_data(filters)
    columns = get_columns()

    return columns, data


def get_data(filters=None):

    sql_string = """
        SELECT

        `tabWht Cert`.`name` AS `wht_cert_id`,

        `tabWht Cert`.`whdee`,
        `tabWht Cert`.`whdee_prefix`,
        `tabWht Cert`.`whdee_name`,
        `tabWht Cert`.`whdee_branch_no`,
        `tabWht Cert`.`workflow_state`,
        `tabWht Cert`.`pnd`,
        `tabWht Cert`.`date`,

        EXTRACT(YEAR FROM `tabWht Cert`.`date`) AS 'year',
        EXTRACT(MONTH FROM `tabWht Cert`.`date`) AS 'month',

        SUM(`tabWht Cert Detail`.`paid`) AS 'paid',
        SUM(`tabWht Cert Detail`.`wht`) AS 'wht',

        `tabPnd Detail`.`parent` AS 'pnd_name'

        FROM `tabWht Cert`

        INNER JOIN `tabWht Cert Detail`
        ON `tabWht Cert Detail`.`parent`=`tabWht Cert`.`name`

        LEFT JOIN `tabPnd Detail`
        ON `tabPnd Detail`.`wht_cert`=`tabWht Cert`.`name`

        """

    if 'whder' in filters:
        sql_string += 'WHERE `tabWht Cert`.`whder`="{name}" '.format(
            name=filters['whder']
            )

    sql_string += """
    GROUP BY `tabWht Cert`.`name`

    ORDER BY `tabWht Cert`.`name` ASC;
    """

    data = frappe.db.sql(sql_string, as_dict=1)

    return data


def get_columns():

    columns = [
        {
            'label': _('Doc No'),
            'fieldtype': 'Link',
            'options': 'Wht Cert',
            'fieldname': 'wht_cert_id',
            'width': 110,
        },
        {
            'label': _('Status'),
            'fieldname': 'workflow_state',
            'width': 80,
        },
        {
            'label': _('Pnd Type'),
            'fieldname': 'pnd',
            'width': 60,
        },
        {
            'label': _('Date'),
            'fieldtype': 'Date',
            'fieldname': 'date',
            'width': 90,
        },
        {
            'label': _('Tax Id'),
            'fieldname': 'whdee',
            'width': 130,
        },
        {
            'label': _('Branch'),
            'fieldname': 'whdee_branch_no',
            'width': 60,
        },
        {
            'label': _('Prefix'),
            'fieldname': 'whdee_prefix',
            'width': 50,
        },
        {
            'label': _('Name'),
            'fieldname': 'whdee_name',
            'width': 120,
        },
        {
            'label': _('Wht Paid'),
            'fieldtype': 'Currency',
            'fieldname': 'paid',
            'width': 100,
        },
        {
            'label': _('Wht Wht'),
            'fieldtype': 'Currency',
            'fieldname': 'wht',
            'width': 100,
        },
        {
            'label': _('Short Pnd'),
            'fieldtype': 'Link',
            'options': 'Pnd',
            'fieldname': 'pnd_name',
            'width': 70,
        },
        {
            'label': _('Month'),
            'fieldname': 'month',
            'width': 50,
        },
        {
            'label': _('Year'),
            'fieldname': 'year',
            'width': 50,
        },
    ]

    return columns
