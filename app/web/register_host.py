# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/3 0003 1:39
# @Author   : Gpp
# @File     : register_host.py
from flask import request, jsonify, current_app

from app.helper.host_crud import HostCrud
from app.web import api
from flask_restful import Resource

@api.resource('/host')
class Host(Resource):
    # url = '/host'
    # url = '/host?id=xx&type=vmess'
    def get(self):
        if not request.json:
            return jsonify({"errCode": 404, "errMsg": "没有找到数据"})

        host_data = request.json['host_data']

        host_dict = {}
        result = HostCrud(host_data).get()
        host_dict.update({'data': result})
        return jsonify(host_dict)

    def post(self):
        if not request.json:
            return {"errCode": 404, "errMsg": "没有收到数据"}
        host_data = request.json['host_data']
        print(host_data)
        result = HostCrud(host_data).post()
        current_app.logger.info(result)
        return jsonify(result)

    def delete(self):
        if not request.json:
            return {"errCode": 404, "errMsg": "没有收到数据"}
        host_data = request.json['host_data']
        result = HostCrud(host_data).delete()
        return 'sd'

    def put(self):
        if not request.json:
            return {"errCode": 404, "errMsg": "没有收到数据"}
        source_data = [request.json['host_data'][0]]
        change_data = request.json['host_data'][1]
        result = HostCrud(source_data).put(change_data)
        return jsonify(result)
