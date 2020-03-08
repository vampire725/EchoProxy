# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/3 0003 1:02
# @Author   : Gpp
# @File     : send_data.py
import requests

data = {"local": "beijing"}
proxy_data = {'proxy_data': [
    {"v": "2",
     "ps": "BWG-LA",
     "add": "65.49.212.111",
     "port": "62860",
     "proxy_id": "523f96fd-a480-4b13-919e-ddd54dee3d71",
     "aid": "233",
     "net": "tcp",
     "type": "none",
     "host": "",
     "path": "",
     "tls": "",
     "proxy_type": "vmess",
     "is_share": True,
     },
    {"v": "2",
     "ps": "GCP-TW",
     "add": "34.80.52.191",
     "port": "45461",
     "proxy_id": "ec6a267e-987d-44a8-aff5-fd646e9b6d87",
     "aid": "233",
     "net": "tcp",
     "type": "none",
     "host": "",
     "path": "",
     "tls": "",
     "proxy_type": "vmess",
     "is_share": True,
     },
    {
        "add": "34.80.60.73",
        "port": "35535",
        "secret": "aes-256-cfb",
        "password": "t14RB2u6D5dA",
        "alias": "GWP-Taiwan",
        "proxy_type": "ss",
        "is_share": True,
    },
    {
        "add": "65.49.212.111",
        "port": "18344",
        "secret": "aes-256-cfr",
        "password": "6D#gpFucT$8a",
        "alias": "BWG-LA",
        "proxy_type": "ss",
        "is_share": True,
    }]}

proxy_data2 = {'proxy_data': [{"aid": "sds", "proxy_type": "vmess", "port": "2344475", "add": "34.56.767.397"},
                              {"add": '45345.6778', "proxy_type": "ss", "port": "237443"}]}

proxy_data3 = {"type": "vmess", "data": [{"port": "234445", "add": "34.56.767.39"}, {"type": "hht", "aid": "sds_"}]}
# a = requests.get('http://127.0.0.1:196/proxy', json=proxy_data)
# print(a.json())
j = requests.post('http://127.0.0.1:196/proxy', json=proxy_data)
# print(type(a.json()), a.json())

# k = requests.put('http://127.0.0.1:196/proxy', json=proxy_data3)
# print(k.status_code)

# d = requests.delete('http://127.0.0.1:196/proxy', json=proxy_data2)


# a = requests.get('http://127.0.0.1:196/generate')
# print(a.json())
