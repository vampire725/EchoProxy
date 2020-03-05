# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 0002 0:42
# @Author   : Gpp
# @File     : register_proxy.py
from flask import request, jsonify

from app.crud.proxy_crud import ProtocolCrud
from app.web import api
from flask_restful import Resource


@api.resource('/proxy')
class Proxy(Resource):
    # url = '/proxy'
    # url = '/proxy?id=xx&type=vmess'
    def get(self):
        if not request.json:
            return jsonify({"errCode": 404, "errMsg": "没有找到数据"})

        proxy_data = request.json['proxy_data']

        vmess_dict = {}
        try:
            result = ProtocolCrud(proxy_data).get_proxy()
        except Exception as e:
            result = [f"出错啦{e}"]
        vmess_dict.update({'data': result})
        return jsonify(vmess_dict)

    def post(self):
        # 新增
        proxy_data = request.json['proxy_data']
        result = ProtocolCrud(proxy_data).post_proxy()
        return result

    def delete(self):
        if not request.json:
            return {"errCode": 404, "errMsg": "没有收到数据"}
        del_data = request.json['proxy_data']
        result = ProtocolCrud(del_data).delete_proxy()
        return result

    def put(self):
        if not request.json:
            return {"errCode": 404, "errMsg": "没有收到数据"}
        source_data = request.json['data'][0]
        change_data = request.json['data'][1]
        data_type = request.json['type']
        result = ProtocolCrud(source_data).put_proxy(data_type, change_data)
        return jsonify(result)
