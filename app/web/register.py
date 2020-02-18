# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 10:09
# @Author   : Gpp
# @File     : register.py
from app.web import web


@web.route('/register')
def register():
    return 'hello'
