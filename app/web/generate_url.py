# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/4 0004 2:09
# @Author   : Gpp
# @File     : generate_url.py
from flask_restful import Resource

from app.web import api


@api.resource('/generate')
class Generate(Resource):
    pass
