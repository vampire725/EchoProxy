# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/23 0023 17:01
# @Author   : Gpp
# @File     : storage_url.py
from app.helper.encrypt import Encrypt
from app.helper.generate_url import GenerateUrl
from echo import app


class StorageProtocol:
    def __init__(self):
        self.my_col = app.config['MY_COL']

    def add_url(self, data: dict):
        user_id = data.get('id') if data.get('id') else ''
        add = data.get('add') if data.get('add') else ''
        port = data.get('port') if data.get('port') else ''
        if self.my_col.find({"user_id": user_id}).count() > 0 \
                or self.my_col.find({"add": add, "port": port}).count() > 0:
            return {"errCode": 111, "errMsg": "此userID已被登记"}
        try:
            encrypt_data = Encrypt.one_encrypting(GenerateUrl(data).url())
            if user_id:
                data.update({"user_id": user_id, "encrypt_data": encrypt_data})
            else:
                data.update({"encrypt_data": encrypt_data})
            self.my_col.insert_one(data)
            return {"errCode": 0, "errMsg": "存储成功"}
        except Exception:
            return {"errCode": 112, "errMsg": "存储发生错误"}

    def delete_url(self):
        pass

    def update_url(self):
        pass

    def fin_url(self):
        pass

    def list_url(self):
        pass
