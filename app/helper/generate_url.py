# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/23 0023 17:32
# @Author   : Gpp
# @File     : generate_url.py

class GenerateUrl:

    def __init__(self, params):
        self.params = params

    def url(self):
        if 'id' in self.params:
            return self._vemess_url()
        else:
            return self._ss_url()

    def _vemess_url(self):
        return "vmess://" + str(self.params)

    def _ss_url(self):
        return f"ss://{self.params['secret']}:{self.params['password']}@{self.params['add']}:{self.params['port']}"

