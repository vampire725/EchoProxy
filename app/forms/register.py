# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 11:45
# @Author   : Gpp
# @File     : register.py
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class RegisterForm(Form):
    ip = StringField(validators=[DataRequired(), Length(min=4, max=25, message="IP地址不和规范")])
    port = IntegerField(validators=[NumberRange(min=2, max=5)], default=1234)
    userID = StringField(validators=[DataRequired(), Length(min=1)])
