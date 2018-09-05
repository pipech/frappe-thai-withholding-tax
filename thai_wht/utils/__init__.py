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


def set_db_host():
    """Preventing lost mysql connection when frappe image change ip addr."""
    import subprocess
    db_host = frappe.conf.db_host
    root_pwd = frappe.conf.root_password
    db_name = frappe.conf.get('db_name')
    update_sql = """
        UPDATE mysql.db
        SET host = '10.%.%.%'
        WHERE host LIKE '10.%.%.%' AND user = '{db_name}';

        UPDATE mysql.user
        SET host = '10.%.%.%'
        WHERE host LIKE '10.%.%.%' AND user = '{db_name}';
    """.format(db_name=db_name)
    process = subprocess.Popen(
        [
            'mysql',
            '-h{}'.format(db_host),
            '-uroot',
            '-p{}'.format(root_pwd),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE
        )
    out, err = process.communicate(update_sql)
    if process.returncode != 0:
        raise Exception('Something failed : {}'.format(err))