# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/24 0024 12:50
# @Author   : Gpp
# @File     : base_mongo.py
from pymongo import MongoClient

my_client = MongoClient('mongodb://root:asd1234@111.33.152.130:10660/')
my_db = my_client["test"]
my_col = my_db["test"]
