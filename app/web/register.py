# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 10:09
# @Author   : Gpp
# @File     : register.py
import os
from flask import request, flash, jsonify, send_from_directory, make_response
from app.models.base_mongo import my_db
from . import web
from app.helper.encrypt import encrypting
from app.helper.generate_url import GenerateUrl
from app.helper.storage_url import StorageProtocol
from app.helper.update_subscribe import add_proxy
from app.helper.check import check


@web.route('/load/<proxy_information>', methods=['POST', 'GET'])
def register(proxy_information):
    if request.method == 'GET':
        response = make_response(send_from_directory('url_file', f'{proxy_information}.txt', as_attachment=True))
        response.headers["Content-Disposition"] = f"attachment; filename={proxy_information}.txt"
        return response
    elif not request.json:
        return 'no json'
    else:
        form_data = request.json

        # 检查数据格式
        check_state = check(form_data)
        # 检查
        if not check_state.get('errCode'):
            protocol = StorageProtocol()
            # 添加数据
            result = protocol.add_url(form_data)
            if not result.get('errCode'):
                print(form_data)
                form_data.pop('_id')
                print(form_data)
                return add_proxy(encrypting(GenerateUrl(form_data).url()))
            else:
                return jsonify(result)
        else:
            return jsonify({'errCode': 400, 'errMsg': '填写数据格式错误'})


# @web.errorhandler(501)
# def handle_501(e):
#     error = ''
#     return jsonify({"errorCode": 501, "errorMsg": error})


@web.route('/agent/')
def agent_information():
    my_col = my_db["test"]
    for x in my_col.find():
        print(x)
        return jsonify(x['name'])
