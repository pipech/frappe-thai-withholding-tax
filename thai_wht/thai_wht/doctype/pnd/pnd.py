# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
import datetime


class Pnd(Document):
    def validate(self):
        pnd_count = count_pnd_submit_no(self)[0]
        if pnd_count.identical_draft >= 1:
            if pnd_count.is_self != 1:
                frappe.throw(_("""There'is draft"""))
        elif pnd_count.total_submit - 1 > self.submit_no:
            frappe.throw(_("""เลขกระโดด ยู๋ฮู"""))
        for d in self.wht_cert:
            wht_cert = frappe.get_doc('Wht Cert', d.wht_cert)
            if wht_cert.workflow_state == 'Submitted':
                frappe.throw(_("""ซัมมิ๊ดแล้วเด้อ"""))

    def on_submit(self):
        for d in self.wht_cert:
            print(d.wht_cert)
            doc = frappe.get_doc('Wht Cert', d.wht_cert)
            doc.workflow_state = 'Submitted'
            doc.save()


@frappe.whitelist()
def autogen():
    """Auto generate Pnd doctype.

    Generate by getting all Wht Cert doctype with 'Confirmed' workflow_state
    then used that list to generate Pnd doctype
    """
    # getting Wht Cert doctype with 'Confirmed' workflow_state
    pnd_list = frappe.db.sql(
        """
            SELECT
                pnd,
                whder,
                whder_branch,
                month(date) AS month,
                year(date) AS year
            FROM `tabWht Cert`
            WHERE
                workflow_state = 'Confirmed'
            GROUP BY
                pnd,
                whder,
                whder_branch,
                month,
                year
        """,
        as_dict=1
    )

    # create new Pnd
    for pnd in pnd_list:
        # using default law
        # TODO(fix law value) we should get law value from somewhere else
        pnd.law = '3 เตรส'

        # don't create new Pnd if there is existing draft document
        pnd_count = count_pnd(pnd)[0]
        if not pnd_count.total_draft >= 1:

            # create new Pnd
            pnd_doc = frappe.get_doc({
                'doctype': 'Pnd',
                'pnd': pnd.pnd,
                'whder': pnd.whder,
                'whder_branch': pnd.whder_branch,
                'month': pnd.month,
                'year': pnd.year,
                'law': pnd.law,
                'submit_no': pnd_count.total_submit,
                'date': datetime.datetime.now(),
            })

            # getting Wht Cert list
            wht_cert_sql = """
                SELECT
                    name
                FROM `tabWht Cert`
                WHERE
                    workflow_state = 'Confirmed' AND
                    pnd = '{pnd}' AND
                    whder = '{whder}' AND
                    whder_branch = '{whder_branch}' AND
                    month(date) = {month} AND
                    year(date) = {year}
            """.format(
                pnd=pnd.pnd,
                whder=pnd.whder,
                whder_branch=pnd.whder_branch,
                month=pnd.month,
                year=pnd.year
            )
            wht_cert_list = frappe.db.sql(
                wht_cert_sql,
                as_dict=1
            )
            # adding Wht Cert to child table
            for wht_cert in wht_cert_list:
                pnd_doc.append('wht_cert', {
                    'wht_cert': wht_cert.name,
                })

            # insert Pnd document
            pnd_doc.insert()

    return 'done'


def count_pnd_submit_no(pnd):
    """Validate existing document before save or submit.

    Args:
        pnd (dict): Pnd object with field value

    Returns:
        dict

    """
    pnd_count_sql = """
        SELECT
            COUNT(IF(
                submit_no={submit_no} AND
                docstatus=0 AND
                name='{name}'
                , 1, NULL))
                AS 'is_self',
            COUNT(IF(submit_no={submit_no} AND docstatus=0, 1, NULL))
                AS 'identical_draft',
            COUNT(IF(submit_no!={submit_no} AND docstatus=1, 1, NULL))
                AS 'total_submit'
        FROM `tabPnd`
        WHERE
            pnd='{pnd}' AND
            whder='{whder}' AND
            whder_branch='{whder_branch}' AND
            month={month} AND
            year={year} AND
            law='{law}'
        """.format(
        name=pnd.name,
        pnd=pnd.pnd,
        whder=pnd.whder,
        whder_branch=pnd.whder_branch,
        month=pnd.month,
        year=pnd.year,
        law=pnd.law,
        submit_no=pnd.submit_no
        )
    pnd_count = frappe.db.sql(
        pnd_count_sql,
        as_dict=1
    )
    return pnd_count


def count_pnd(pnd):
    """Count existing doc before generate.

    Args:
        pnd (dict): Pnd object with field value

    Returns:
        dict

    """
    pnd_count_sql = """
        SELECT
            COUNT(IF(docstatus=0, 1, NULL))
                AS 'total_draft',
            COUNT(IF(docstatus=1, 1, NULL))
                AS 'total_submit'
        FROM `tabPnd`
        WHERE
            pnd='{pnd}' AND
            whder='{whder}' AND
            whder_branch='{whder_branch}' AND
            month={month} AND
            year={year} AND
            law='{law}'
        """.format(
        pnd=pnd.pnd,
        whder=pnd.whder,
        whder_branch=pnd.whder_branch,
        month=pnd.month,
        year=pnd.year,
        law=pnd.law,
        submit_no=pnd.submit_no
        )
    pnd_count = frappe.db.sql(
        pnd_count_sql,
        as_dict=1
    )
    return pnd_count
