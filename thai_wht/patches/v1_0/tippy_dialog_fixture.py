import frappe

from thai_wht.setup.install import add_fixture


def execute():
    add_fixture(only=['user_progress'])
