# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/23 0023 15:14
# @Author   : Gpp
# @File     : encrypt.py
import json
from base64 import b64encode


class Encrypt:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def one_encrypting(data):
        protocol, detail = data.split('//')
        detail_b64 = b64encode(detail.encode('utf-8')).decode('utf-8')
        return f"{protocol}//{detail_b64}\n"

    @staticmethod
    def two_encrypting(data):
        url_b64 = b64encode(data.encode('utf-8')).decode('utf-8')
        return url_b64

