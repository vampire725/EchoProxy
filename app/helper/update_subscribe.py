# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/24 0024 16:03
# @Author   : Gpp
# @File     : update_subscribe.py


def add_proxy(data):
    try:
        with open('app/url_file/proxy_information.txt', 'w', encoding='utf-8')as f:
            f.write(data)
        return {"errCode": 0, "errMsg": "存储成功"}
    except Exception as e:
        return {"errCode": 404, "errMsg": f"出错啦{e}"}
