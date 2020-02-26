# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/25 0025 10:52
# @Author   : Gpp
# @File     : send_data.py
import json
from msilib import text

import requests

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
    "tls": "",
}
example2 = {
    "add": "34.80.60.73",
    "port": 35535,
    "secret": "aes-256-cfb",
    "password": "t14RB2u6D5dA",
}
example3 = {
    "v": "2",
    "ps": "BWG-LA",
    "add": "65.49.212.111",
    "port": "62860",
    "id": "523f96fd-a480-4b13-919e-ddd54dee3d71",
    "aid": "233",
    "net": "tcp",
    "type": "none",
    "host": "",
    "path": "",
    "tls": "",
}

# form_data = json.loads(json.dumps(example))
# print(form_data)
# ip = dict(example).get('add')
# print(ip)
r = requests.post("http://127.0.0.1:757/load/file", json=example)
