# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 0002 0:33
# @Author   : Gpp
# @File     : __init__.py.py
from flask import Blueprint
from flask_restful import Api

web = Blueprint('web', __name__)
api = Api(web)
from app.web import register_proxy
from app.web import register_host
