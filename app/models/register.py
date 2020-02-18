# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 11:34
# @Author   : Gpp
# @File     : register.py
from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Register(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30), default='111.33.150.132')
    port = Column(Integer, default=1234)
    userID = Column(String(100), nullable=False, unique=True)
    alterID = Column(String(100))
