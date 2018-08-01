# -*- coding: utf-8 -*-
# Copyright (c) 2018, SpaceCode Co., Ltd. and contributors
# For license information, please see license.txt


def check_tax_id(id):

    if len(id) != 13:
        return False

    # ขั้นตอนที่ 1 - เอาเลข 12 หลักมา แยกเป็น list
    # หลักที่ 13 ใช้ตรวจสอบผลลัพธ์
    list_id = list(id)

    sum = 0
    for index in range(0, 12):
        # ขั้นตอนที่ 1.5 - เช็คว่าแต่ละตำแหน่งเป็นตัวเลขหรือไม่
        try:
            int_id = int(list_id[index])
        except ValueError:
            return False
        # ขั้นตอนที่ 2 - เอาเลข 12 หลักนั้นมา คูณเข้ากับเลขประจำหลักของมัน
        index_value = int_id * (13 - index)
        # ขั้นตอนที่ 3 - เอาผลคูณทั้ง 12 ตัวมา บวกกันทั้งหมด
        sum += index_value

    # ขั้นตอนที่ 4 - เอาเลขที่ได้จากขั้นตอนที่ 3 มา mod 11 (หารเอาเศษ)
    remainder = sum % 11

    # ขั้นตอนที่ 5 - เอา 11 ตั้ง ลบออกด้วย เลขที่ได้จากขั้นตอนที่ 4
    # ถ้าเกิด ลบแล้วได้ออกมาเป็นเลข 2 หลัก ให้เอาเลขในหลักหน่วย มาใช้
    digit13 = (11 - remainder) % 10

    # ตรวจสอบ ค่าที่ได้ กับ เลขตัวสุดท้ายของ บัตรประจำตัวประชาชน
    if digit13 == int(list_id[12]):
        return True
    else:
        return False
