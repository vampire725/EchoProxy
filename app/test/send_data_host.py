# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 1:31
# @Author   : Gpp
# @File     : send_data_host.py
import requests

host_data = {"host_data": [{"operator": "hostwinds",
                            "local": "西雅图",
                            "bandwidth": 111,
                            "flow_limit": 11.11,
                            "ip": "104.168.206.66",
                            "ssh_port": 22,
                            "ssh_user": "root",
                            "ssh_pass": "MJMJVTj7KM8Ygr2f",
                            },
                           {"operator": "hostwinds",
                            "local": "西雅图",
                            "bandwidth": 111,
                            "flow_limit": 11.11,
                            "ip": "104.168.220.106",
                            "ssh_port": 22,
                            "ssh_user": "root",
                            "ssh_pass": "8MH8JQB34CxPret",
                            },
                           {"operator": "hostwinds",
                            "local": "达拉斯",
                            "bandwidth": 111,
                            "flow_limit": 11.11,
                            "ip": "23.254.211.110",
                            "ssh_port": 22,
                            "ssh_user": "root",
                            "ssh_pass": "2cK6tYzSGaa4JnSd",
                            }
                           ]}
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
