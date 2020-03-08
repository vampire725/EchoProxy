# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 0002 0:33
# @Author   : Gpp
# @File     : __init__.py.py
import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_docs import ApiDoc

from app.models.base import db

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')
    register_blueprint(app)
    register_logging(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(echo):
    from app.web import web
    echo.register_blueprint(web)


def register_logging(app):
    app.logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = RotatingFileHandler(os.path.join(basedir, 'logs/my_log'),
                                       maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    if not app.debug:
        app.logger.addHandler(file_handler)
