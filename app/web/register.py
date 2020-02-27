# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 10:09
# @Author   : Gpp
# @File     : register_base_test.py
import os
from flask import request, flash, jsonify, send_from_directory, make_response
from . import web
from app.helper.encrypt import Encrypt
from app.helper.storage_url import StorageProtocol
from app.helper.update_subscribe import add_proxy
from app.helper.check import check


@web.route('/register', methods=['POST', 'GET'])
def register():
    if not request.json:
        return 'no json'
    else:
        form_data = request.json
        check_state = check(form_data)
        protocol = StorageProtocol()
        if not check_state.get('errCode'):
            return protocol.add_url(form_data)
        else:
            return jsonify({'errCode': 400, 'errMsg': '填写数据格式错误'})


@web.route('/load/<proxy_information>', methods=['POST', 'GET'])
def generate_subscript_file(proxy_information):
    if not request.json:
        response = make_response(send_from_directory('url_file', f'{proxy_information}.txt', as_attachment=True))
        response.headers["Content-Disposition"] = f"attachment; filename={proxy_information}.txt"
        return response
    else:
        data = request.json['data']
        encrypt_str = []
        for url_data in data:
            encrypt_str.append(url_data['encrypt_data'])
        return add_proxy(Encrypt.two_encrypting(''.join(encrypt_str)))
