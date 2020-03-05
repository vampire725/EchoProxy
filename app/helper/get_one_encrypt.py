# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 20:55
# @Author   : Gpp
# @File     : get_one_encrypt.py
from flask import current_app

from app.helper.encrypt import one_vmess_encrypting, one_ss_encrypting
from app.models.protocol_template import VmessProtocol, SsProtocol


def get_one_encrypt_data(proxies):
    one_encrypt = []
    for proxy in proxies:
        if proxy.proxy_type == 'vmess':
            # 生成规范协议链接
            url = VmessProtocol(proxy.__dict__).vmess_url()
            current_app.logger.info({"errCode": 0, "errMsg": f"生成{url}"})
            # 对链接进行第一次加密
            one_encrypt.extend(one_vmess_encrypting(url))
        else:
            url, alias = SsProtocol(proxy.__dict__).ss_url()
            current_app.logger.info({"errCode": 0, "errMsg": f"生成{url}"})
            one_encrypt.extend(one_ss_encrypting(url, alias))
    return one_encrypt
