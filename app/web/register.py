# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 10:09
# @Author   : Gpp
# @File     : register.py
import json

from flask import request, flash, jsonify
from app.models.base_mongo import my_db
from . import web
from app.helper.encrypt import encrypting
from app.helper.generate_url import GenerateUrl
from app.helper.storage_url import StorageProtocol
from app.helper.update_subscribe import add_proxy
from ..helper.check import check


@web.route('/register', methods=['POST', 'GET'])
def register():
    # form_data = RegisterForm(request.form)
    form_data = json.loads(request.data)
    check_state = check(form_data)
    if not check_state.get('errCode'):
        protocol = StorageProtocol()
        generate_url = GenerateUrl(form_data)
        # 添加数据
        result = protocol.add_url(form_data)
        if result.get('errCode') == 111:
            return jsonify(result)
        if not result:
            return add_proxy(encrypting(generate_url.url()))
        else:
            return jsonify({"state": 500, "msg": "存储发生错误"})
    else:
        flash('填写数据格式错误')


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
