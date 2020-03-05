# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 2:09
# @Author   : Gpp
# @File     : obtain_url.py
from app.web import api
from flask_restful import Resource
from flask import make_response, send_from_directory,jsonify
from app.helper.encrypt import two_encrypting
from app.crud.proxy_crud import ProtocolCrud
from app.helper.get_one_encrypt import get_one_encrypt_data
from app.helper.update_subscribe import add_proxy


@api.resource('/generate')
class Generate(Resource):
    def get(self):
        proxies = ProtocolCrud.get_all_share()
        one_encrypt = get_one_encrypt_data(proxies)
        result = add_proxy(two_encrypting(''.join(one_encrypt)))
        return jsonify(result)


@api.resource('/load/<proxy_information>')
class GetUrl(Resource):
    def get(self, proxy_information):
        response = make_response(send_from_directory('url_file', f'{proxy_information}.txt', as_attachment=True))
        response.headers["Content-Disposition"] = f"attachment; filename={proxy_information}.txt"
        return response
