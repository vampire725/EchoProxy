# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/23 0023 15:14
# @Author   : Gpp
# @File     : encrypt.py
from base64 import b64encode


def encrypting(url: str):
    protocol, detail = url.split('//')
    detail_b64 = b64encode(detail.encode('utf-8')).decode('utf-8')
    url_b64 = b64encode((protocol + '//' + detail_b64).encode('utf-8')).decode('utf-8')

    return url_b64

