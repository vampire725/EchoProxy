# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 0:19
# @Author   : Gpp
# @File     : host_crud.py
from app import db
from app.models.host_proxy import Host
from app.models.host_template import HostTemplate


class HostCrud:
    def __init__(self, data):
        self.data = data
        self.hosts = []
        for host in data:
            self.hosts.extend(Host.query.filter_by(**host).all())

    def get(self):
        data_list = []
        for host_data in self.hosts:
            data_list.append(HostTemplate(host_data).__dict__)
        return data_list

    def post(self):
        for host in self.data:
            h = Host(**host)
            db.session.add(h)
        try:
            db.session.commit()
            return {"errCode": 0, "errMsg": "存储成功"}
        except Exception as e:
            # logger
            return {"errCode": 1, "errMsg": f"{e}存储失败"}

    def put(self, change_data):
        result = self.hosts[0]
        result.set_attrs(change_data)
        db.session.commit()

    def delete(self):
        for host in self.hosts:
            db.session.delete(host)
        db.session.commit()
