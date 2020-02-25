# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/24 0024 16:03
# @Author   : Gpp
# @File     : update_subscribe.py


def add_proxy(data):
    try:
        with open('app/url_file/proxy_information.txt', 'a', encoding='utf-8')as f:
            f.write(data + '\n')
        return {"errCode": 0, "errMsg": "存储成功"}
    except Exception:
        return {"errCode": 404, "errMsg": "发生未知错误"}
