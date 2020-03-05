# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/3 0003 11:11
# @Author   : Gpp
# @File     : proxy_crud.py
from flask import current_app

from app import db
from app.models.host_proxy import ProxyVmess, ProxySs


class ProtocolCrud:

    def __init__(self, data):
        self.data = data

    def get_proxy(self):
        data_list = []
        find_vmess, find_ss = self.get_part_proxy()
        for proxy in find_vmess:
            proxy_dict = proxy.__dict__
            proxy_dict.pop('_sa_instance_state')
            data_list.append(proxy_dict)
        current_app.logger.info({"errCode": 0, "errMsg": f"找到{self.data}数据"})
        for proxy in find_ss:
            proxy_dict = proxy.__dict__
            proxy_dict.pop('_sa_instance_state')
            data_list.append(proxy_dict)
        current_app.logger.info({"errCode": 0, "errMsg": f"找到{self.data}"})
        return data_list

    def get_part_proxy(self):
        vmess_list = []
        ss_list = []
        for proxy_field in self.data:
            if proxy_field['proxy_type'] == 'vmess':
                vmess_list.extend(ProxyVmess.query.filter_by(**proxy_field).all())
            else:
                ss_list.extend(ProxySs.query.filter_by(**proxy_field).all())
        return vmess_list, ss_list

    @staticmethod
    def get_all_share():
        proxies = []
        proxies.extend(ProxyVmess.query.filter_by(is_share=True).all())
        proxies.extend(ProxySs.query.filter_by(is_share=True).all())
        return proxies

    def post_proxy(self):
        for proxy in self.data:
            proxy['id'] = '-'.join([proxy['add'], proxy['port']])
            if proxy.get('proxy_type') == 'vmess':
                proxy = ProxyVmess(**proxy)
            elif proxy.get('proxy_type') == 'ss':
                proxy = ProxySs(**proxy)
            else:
                current_app.logger.debug({"errCode": 1, "errMsg": "数据已存在"})
            db.session.add(proxy)
        try:
            db.session.commit()
            current_app.logger.info({"errCode": 0, "errMsg": f"存储成功{self.data}"})
            return {"errCode": 0, "errMsg": "存储成功"}
        except Exception as e:
            current_app.logger.error({"errCode": 1, "errMsg": f"{e}存储失败"})
            return {"errCode": 1, "errMsg": f"{e}存储失败"}

    def put_proxy(self, proxy_type, data2):
        if proxy_type == 'vmess':
            results = ProxyVmess.query.filter_by(**self.data).first()
        else:
            results = ProxySs.query.filter_by(**self.data).first()
        results.set_attrs(data2)
        try:
            db.session.commit()
            current_app.logger.info({"errCode": 0, "errMsg": f"修改{self.data}为{data2}成功"})
        except Exception as e:
            current_app.logger.error({"errCode": 1, "errMsg": f"修改{self.data}{e}出错了"})
        return f'{results}修改成功'

    def delete_proxy(self):
        vmess_result, ss_result = self.get_part_proxy()
        for ss in ss_result:
            db.session.delete(ss)
        for vmess in vmess_result:
            db.session.delete(vmess)
        try:
            db.session.commit()
            current_app.logger.info({"errCode": 0, "errMsg": f"删除{self.data}成功"})
            return {"errCode": 0, "errMsg": "删除成功"}
        except Exception as e:
            current_app.logger.error({"errCode": 1, "errMsg": f"删除{self.data}{e}出错了"})
            return {"errCode": 1, "errMsg": f"{e}存储失败"}
