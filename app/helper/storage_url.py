# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/23 0023 17:01
# @Author   : Gpp
# @File     : storage_url.py
from app.models.base_mongo import my_db


class StorageProtocol:
    @staticmethod
    def add_url(data: dict):
        my_col = my_db["test"]
        user_id = data.get('user_id') if data.get('user_id') else ''
        add = data.get('add') if data.get('add') else ''
        port = data.get('port') if data.get('port') else ''
        if my_col.find({"user_id": user_id}).count() > 0 \
                or my_col.find({"add": add, "port": port}).count() > 0:
            return {"errCode": 111, "errMsg": "此userID已被登记"}
        try:
            my_col.insert_one(data)
            return {"errCode": 0, "errMsg": "存储成功"}
        except Exception:
            return {"errCode": 112, "errMsg": "存储错误"}

    def delete_url(self):
        pass

    def update_url(self):
        pass

    def view_url(self):
        pass

    def list_url(self):
        pass
