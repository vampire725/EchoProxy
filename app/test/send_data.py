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
    "ps": "BWG-LA",
    "add": "65.49.212.111",
    "port": "62860",
    "id": "523f96fd-a480-4b13-919e-ddd54dee3d71",
    "aid": "233",
    "net": "tcp",
    "type": "none",
    "host": "",
    "path": "",
    "tls": ""
}
example2 = {
    "add": "65.49.212.111",
    "port": 18344,
    "secret": "aes-256-ctr",
    "password": "6D#gpFucT$8a"
}

# form_data = json.loads(json.dumps(example))
# print(form_data)
# ip = dict(example).get('add')
# print(ip)
r = requests.post("http://127.0.0.1:757/load/file", json=example2)
