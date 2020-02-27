# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 9:52
# @Author   : Gpp
# @File     : __init__.py.py

from flask import Flask

from app.test.base_test import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.settings')
    app.config.from_object('app.secure')
    register_blueprint(app)
    # db.init_app(app)
    # db.create_all(app=app)
    return app

def register_blueprint(echo):
    from app.web import web
    echo.register_blueprint(web)

