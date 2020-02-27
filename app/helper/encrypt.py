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


if __name__ == '__main__':
    test_dict = {
        "v": "2",
        "ps": "GCP-TW",
        "add": "34.80.52.191",
        "port": "45461",
        "id": "ec6a267e-987d-44a8-aff5-fd646e9b6d87",
        "aid": "233",
        "net": "tcp",
        "type": "none",
        "host": "",
        "path": "",
        "tls": ""
    }

    json_str = str(test_dict)
    pass
    encrypting(f'vmess://{json_str}')

# def add_encrypt_proxy(url):
#     protocol, detail = url.split('//')
#     detail_b64 = b64encode(detail.encode('utf-8')).decode('utf-8')
#     try:
#         with open('app/url_file/proxy_information.txt', 'a+', encoding='utf-8')as f:
#             line = f.readline(5)
#             if not line:
#                 f.write(b64encode((protocol + '//' + detail_b64).encode('utf-8')).decode('utf-8'))
#             else:
#                 f.write(b64encode(('\n' + protocol + '//' + detail_b64).encode('utf-8')).decode('utf-8'))
#         return {"errCode": 0, "errMsg": "存储成功"}
#     except Exception:
#         return {"errCode": 404, "errMsg": "发生未知错误"}
