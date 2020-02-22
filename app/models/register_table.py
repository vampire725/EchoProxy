# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 11:34
# @Author   : Gpp
# @File     : register_table.py
from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Register(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30))
    port = Column(Integer)
    userID = Column(String(100), nullable=False, unique=True)
    alterID = Column(String(100))
