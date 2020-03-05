# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 0:34
# @Author   : Gpp
# @File     : host_template.py
class HostTemplate:
    def __init__(self, data):
        self.id = data.id
        self.operator = data.operator
        self.local = data.local
        self.bandwidth = data.bandwidth
        self.flow_limit = data.flow_limit
        self.ip = data.ip
        self.ssh_port = data.ssh_port
        self.ssh_user = data.ssh_user
        self.ssh_pass = data.ssh_pass
