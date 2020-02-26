# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/26 0026 11:37
# @Author   : Gpp
# @File     : encrypt_test.py
from base64 import b64encode
import json
example = {
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
example2 = {
    "add": "34.80.60.73",
    "port": 35535,
    "secret": "aes-256-cfb",
    "password": "t14RB2u6D5dA"
}
print(str(example))
url = "vmess://" + str(example)
url2 = "ss://aes-256-cfb:6D#gpFucT$8a@65.49.212.111:18344"
print(url)
protocol, detail = url.split('//')
detail_b64 = b64encode((detail+'\n').encode('utf-8')).decode('utf-8')
print(b64encode(('\n'+protocol + '//' + detail_b64+'\n').encode('utf-8')).decode('utf-8'))
example = {
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
url = "vmess://" + str(example)
