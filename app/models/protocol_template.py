# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/3 0003 16:56
# @Author   : Gpp
# @File     : protocol_template.py
class VmessProtocol:
    def __init__(self, proxy):
        print(proxy.aid)
        self.v = proxy.v if proxy.v else ''
        self.ps = proxy.ps if proxy.ps else ''
        self.add = proxy.add if proxy.add else ''
        self.port = proxy.port if proxy.port else ''
        self.id = proxy.proxy_id if proxy.proxy_id else ''
        self.aid = proxy.aid if proxy.aid else '233'
        self.net = proxy.net if proxy.net else 'tcp'
        self.type = proxy.type if proxy.type else 'none'
        self.host = proxy.host if proxy.host else ''
        self.path = proxy.path if proxy.path else ''
        self.tls = proxy.tls if proxy.tls else ''


class SsProtocol:
    def __init__(self, proxy):
        self.add = proxy.add if proxy.add else ''
        self.port = proxy.port if proxy.port else ''
        self.secret = proxy.secret if proxy.secret else ''
        self.password = proxy.password if proxy.password else ''
        self.alias = proxy.alias if proxy.alias else ''
