# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 1:31
# @Author   : Gpp
# @File     : send_data_host.py
import requests

host_data = {"host_data": [{"operator": "111",
                            "local": "111",
                            "bandwidth": 111,
                            "flow_limit": 11.11,
                            "ip": "111",
                            "ssh_port": 111,
                            "ssh_user": "111",
                            "ssh_pass": "111",
                            }]}
host_data2 = {"host_data": [{"operator": "111",
                             "local": "111",
                             }, {"operator": "112",
                                 "local": "112",
                                 }]}
# a = requests.get('http://127.0.0.1:196/host', json=host_data2)
# print(a.json())
j = requests.post('http://127.0.0.1:196/host', json=host_data)
print(j.status_code)

# k = requests.put('http://127.0.0.1:196/host', json=host_data2)
# print(k.status_code)


# d = requests.delete('http://127.0.0.1:196/host', json=host_data2)
