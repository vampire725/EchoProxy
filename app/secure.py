# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 9:54
# @Author   : Gpp
# @File     : secure.py
from pymongo import MongoClient

HOST = '0.0.0.0'
PORT = '757'
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:asd1234@111.33.152.130:10659/echo'

# MONGO_URI = "mongodb://root:asd1234@111.33.152.130:10660/admin"

SECRET_KEY = '\x88D\x91'

my_client = MongoClient('mongodb://root:asd1234@111.33.152.130:10660/')
MY_COL = my_client["test"]['test']
