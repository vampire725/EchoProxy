# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 0:19
# @Author   : Gpp
# @File     : host_crud.py
from flask import current_app

from app import db
from app.models.host_proxy import Host


class HostCrud:
    def __init__(self, data):
        self.data = data
        self.hosts = []
        for host in data:
            self.hosts.extend(Host.query.filter_by(**host).all())

    def get(self):
        data_list = []
        for host_data in self.hosts:
            host_dict = host_data.__dict__
            host_dict.pop('_sa_instance_state')
            data_list.append(host_dict)
        current_app.logger.info({"errCode": 0, "errMsg": f"获取{data_list}"})
        return data_list

    @staticmethod
    def post(data):
        for host in data:
            h = Host(**host)
            db.session.add(h)
        try:
            db.session.commit()
            current_app.logger.info({"errCode": 0, "errMsg": f"{data}存储成功"})
            return {"errCode": 0, "errMsg": "存储成功"}
        except Exception as e:
            current_app.logger.error({"errCode": 1, "errMsg": f"{e}存储失败"})
            return {"errCode": 1, "errMsg": f"{e}存储失败"}

    def put(self, change_data):
        for result in self.hosts:
            result.set_attrs(change_data)
        try:
            db.session.commit()
            current_app.logger.error({"errCode": 0, "errMsg": f"{change_data}修改成功"})
        except Exception as e:
            current_app.logger.error({"errCode": 1, "errMsg": f"{e}修改失败"})

    def delete(self):
        for host in self.hosts:
            db.session.delete(host)
        try:
            db.session.commit()
            current_app.logger.info({"errCode": 200, "errMsg": f"{self.hosts}删除成功"})
        except Exception as e:
            current_app.logger.error({"errCode": 500, "errMsg": f"{e}删除失败"})
