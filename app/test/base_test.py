# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 11:11
# @Author   : Gpp
# @File     : base_test.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()

class Base(db.Model):
    # 告诉flask，这是抽象表，不需要创建
    __abstract__ = True

    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':  # 避免id被改写
                setattr(self, key, value)
