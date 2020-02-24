# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/24 0024 20:18
# @Author   : Gpp
# @File     : check.py
import ipaddress
from flask import abort


def check(data: dict):
    ip = data.get('add')
    port = data['port']
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return {"errCode": 1001, "errMsg": "IP数据格式不正确"}

    try:
        int(port)
    except Exception:
        return {"errCode": 1002, "errMsg": "PORT数据格式不正确"}
    if not 0 < int(port) < 65535:
        return {"errCode": 1002, "errMsg": "PORT数据格式不正确"}
    return {"errCode": 0}


print(check({"add": "65.49.212.11", "port": "854ss"}))
