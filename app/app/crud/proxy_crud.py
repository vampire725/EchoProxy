# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/3 0003 11:11
# @Author   : Gpp
# @File     : proxy_crud.py
from app import db
from app.models.host_proxy import ProxyVmess, ProxySs


class ProtocolCrud:

    def __init__(self, data):
        self.data = data

    def get_proxy(self):
        data_list = []
        find_vmess, find_ss = self.get_part_proxy()
        for proxy in find_vmess:
            data_list.append(proxy.__dict__)
        for proxy in find_ss:
            data_list.append(proxy.__dict__)
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
                # logger
                print({"errCode": 1, "errMsg": "数据已存在"})
            db.session.add(proxy)
        try:
            db.session.commit()
            return {"errCode": 0, "errMsg": "存储成功"}
        except Exception as e:
            # logger
            return {"errCode": 1, "errMsg": f"{e}存储失败"}

    def put_proxy(self, proxy_type, data2):
        if proxy_type == 'vmess':
            results = ProxyVmess.query.filter_by(**self.data).all()
        else:
            results = ProxySs.query.filter_by(**self.data).all()
        results.set_attrs(data2)
        db.session.commit()
        return f'{results}修改成功'

    def delete_proxy(self):
        vmess_result, ss_result = self.get_part_proxy()
        for ss in ss_result:
            db.session.delete(ss)
        for vmess in vmess_result:
            db.session.delete(vmess)
        try:
            db.session.commit()
            return {"errCode": 0, "errMsg": "删除成功"}
        except Exception as e:
            # logger
            return {"errCode": 1, "errMsg": f"{e}存储失败"}
