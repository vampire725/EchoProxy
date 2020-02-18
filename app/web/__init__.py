# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 9:59
# @Author   : Gpp
# @File     : __init__.py.py
from flask import Blueprint

web = Blueprint('web', __name__)
from app.web import register
