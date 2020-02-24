# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/23 0023 17:01
# @Author   : Gpp
# @File     : storage_url.py
from app.models.base_mongo import my_db


class StorageProtocol:
    @staticmethod
    def add_url(data):
        my_col = my_db["test"]
        if my_col.find({"id": data['id']}).count() > 0 or my_col.find({"add": data['add'], "port": data['port']}):
            return {"errCode": 111, "errMsg": "此userID已被登记"}
        try:
            my_col.insert_one(data)
        except Exception:
            return {"errCode": 112, "errMsg": "存储错误"}
        return {"errCode": 0, "errMsg": "存储成功"}

    def delete_url(self):
        pass

    def update_url(self):
        pass

    def view_url(self):
        pass

    def list_url(self):
        pass
