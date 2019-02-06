# -*- coding: utf-8 -*-
# Copyright (c) 2013, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import os
import zipfile

from six import string_types
from thai_wht.thai_wht.report.pnd_attach.pnd_attach import execute


@frappe.whitelist()
def download(name):
    data = execute(name, csv=True)
    pnd = data[0]['pnd']

    # fill main
    data_m = [''] * 47
    if pnd['pnd'] == '3':
        data_m[3] = 'PND3'
        data_m[6] = pnd['whder']
        data_m[44] = 'C'
        data_m = fill_main_fixed(data, data_m, 7)
    elif pnd['pnd'] == '53':
        data_m[3] = 'PND53'
        data_m[44] = pnd['whder']
        data_m = fill_main_fixed(data, data_m, 6)

    # fill detail
    data_d = [None] * len(data)
    if pnd['pnd'] == '3':
        for i, d in enumerate(data):
            dd = [''] * 41
            dd[3] = d['idx']
            dd[4] = d['whdee']
            dd[6] = d['whdee_prefix']
            dd[7] = d['whdee_name']
            dd[39] = d['whdee_branch_no']
            dd = fill_detail_fixed(d, dd, 21)
            data_d[i] = dd
    if pnd['pnd'] == '53':
        for i, d in enumerate(data):
            dd = [''] * 42
            dd[3] = d['idx']
            dd[5] = d['whdee']
            dd[6] = d['whdee_branch_no']
            dd[8] = d['whdee_prefix']
            dd[9] = d['whdee_name']
            dd = fill_detail_fixed(d, dd, 22)
            data_d[i] = dd

    data_m_txt = to_utf8_decimal([data_m])
    data_d_txt = to_utf8_decimal(data_d)

    # file name
    if pnd['whder_branch_no'] == '00000':
        n_branch = 'OZZZZZ'
    else:
        n_branch = 'V{}'.format(pnd['whder_branch_no'])

    n_pnd = str(pnd['pnd'])
    n_pnd = n_pnd.zfill(2)
    n_pnd = 'P{}'.format(n_pnd)

    file_name = '{id}{branch}{pnd}{year}{month}{submit_no}'.format(
        id=pnd['whder'],
        branch=n_branch,
        pnd=n_pnd,
        year=pnd['_year'],
        month=str(pnd['month']).zfill(2),
        submit_no=str(pnd['submit_no']).zfill(4),
    )

    # temp file name
    hash_name = frappe.generate_hash()
    d_path = os.path.join(
        '/tmp',
        '{}D.txt'.format(hash_name)
        )
    m_path = os.path.join(
        '/tmp',
        '{}M.txt'.format(hash_name)
        )
    zip_path = os.path.join(
        '/tmp',
        '{}zip.zip'.format(hash_name)
        )

    # write to txt file
    # using CRLF as new line as instruct in revenue department manual
    with open(m_path, 'w') as f:
        for item in data_m_txt:
            f.write('{}\r\n'.format(item))
    with open(d_path, 'w') as f:
        for item in data_d_txt:
            f.write('{}\r\n'.format(item))

    # zip file
    zip_file = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    zip_file.write(m_path, '{}M.txt'.format(file_name))
    zip_file.write(d_path, '{}D.txt'.format(file_name))
    zip_file.close()

    # get read file to use for frappe response
    fileobj = open(zip_path, 'rb')
    filedata = fileobj.read()
    fileobj.close()

    # delete file
    if os.path.exists(d_path):
        os.remove(d_path)
    if os.path.exists(m_path):
        os.remove(m_path)
    if os.path.exists(zip_path):
        os.remove(zip_path)

    # frappe response
    frappe.local.response.filename = '{name}.txt'.format(
        name=file_name,
        )
    frappe.local.response.filecontent = filedata
    frappe.local.response.type = 'download'


def to_utf8_decimal(data_list):
    """Convert utf8 to Revenue Department format."""
    lines = [None] * len(data_list)
    for idx, data in enumerate(data_list):
        # convert data list to string
        _data = []
        for d in data:
            if isinstance(d, string_types):
                _data.append(d)
            else:
                _data.append(str(d))
        lines_hex = '|'.join(_data)
        # convert string to uft8 code points byte format
        lines_hex = lines_hex.encode('utf-8')
        # convert byte to list of byte array
        lines_hex = list(bytearray(lines_hex))

        line = ''
        sum = 0
        # loop through each unicode code
        for hex in lines_hex:
            # get sum of all hex
            sum = sum + int(hex)
            # convert hex format to decimal with 4 leading zero
            hex = str(hex).zfill(4)
            # add converted utf8 decimal to line string
            line = line + hex
        # adding last 4 digit of sum to line string
        last_four = abs(sum) % 10000
        line = line + str(last_four).zfill(4)

        # add line to lines list
        lines[idx] = line

    return lines


def fill_detail_fixed(row_data, row_data_d, list_idx):
    detail_field = [
        'date',
        'type',
        'rate',
        'paid',
        'wht',
        'condition',
    ]

    for multi in range(3):
        for num, field in enumerate(detail_field):
            key = '{field}{multi}'.format(field=field, multi=multi)
            col = list_idx + num + (multi * 6)
            if key in row_data:
                if field == 'paid' or field == 'wht':
                    row_data[key] = '{0:.2f}'.format(row_data[key])
                row_data_d[col] = row_data[key]

    return row_data_d


def fill_main_fixed(data, data_m, i):
    pnd = data[0]['pnd']
    total = data[0]['total']

    if pnd['whder_branch_no'] == '00000':
        data_m[i] = 'O'
    else:
        data_m[i] = 'V'
    data_m[i+1] = pnd['whder_branch_no']
    data_m[i+2] = pnd['submit_no']
    data_m[i+3] = pnd['month']
    data_m[i+4] = str(pnd['_year'])
    if pnd['law'] == '3 เตรส':
        data_m[i+5] = 1
    elif pnd['law'] == '48 ทวิ':
        data_m[i+6] = 1
    elif pnd['law'] == '50 (3) (4) (5)':
        data_m[i+7] = 1

    data_m[i+8] = total['line']
    data_m[i+9] = '{0:.2f}'.format(total['all_paid'])
    data_m[i+10] = '{0:.2f}'.format(total['all_wht'])
    data_m[i+11] = '{0:.2f}'.format(pnd['penalty'])
    data_m[i+12] = '{0:.2f}'.format(total['all'])
    data_m[i+13] = '{0:.2f}'.format(total['all'])

    data_m[i+15] = '5.1'

    data_m[45] = '2'
    data_m[46] = '2'

    return data_m
