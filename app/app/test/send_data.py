# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/3 0003 1:02
# @Author   : Gpp
# @File     : send_data.py
import requests

data = {"local": "beijing"}
proxy_data = {'proxy_data': [{"port": "234445", "add": "34.56.767.39", "proxy_type": "vmess"},
                             {"add": '45345.67', "proxy_type": "ss"}]}

proxy_data2 = {'proxy_data': [{"aid": "sds", "proxy_type": "vmess", "port": "234445", "add": "34.56.767.39"},
                              {"add": '45345.678', "proxy_type": "ss", "port": "23443"}]}

proxy_data3 = {"type": "vmess", "data": [{"port": "234445", "add": "34.56.767.39"}, {"type": "hh", "aid": "sds"}]}
# a = requests.get('http://127.0.0.1:196/proxy', json=proxy_data)
# print(a.json())
# j = requests.post('http://127.0.0.1:196/proxy', json=proxy_data2)
# print(type(a.json()), a.json())

# k = requests.put('http://127.0.0.1:196/proxy', json=proxy_data3)
# print(k.status_code)

# d = requests.delete('http://127.0.0.1:196/proxy', json=proxy_data2)


a = requests.get('http://127.0.0.1:196/generate')
print(a.json())
