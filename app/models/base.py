# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 0002 22:08
# @Author   : Gpp
# @File     : base.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
