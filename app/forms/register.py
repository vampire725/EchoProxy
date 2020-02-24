# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 11:45
# @Author   : Gpp
# @File     : register.py
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from app.models.base_mongo import my_col
from app.models.register import Register


class RegisterForm(Form):
    ip = StringField(validators=[DataRequired(), Length(min=4, max=25, message="IP地址不合规范")])
    port = IntegerField(validators=[NumberRange(min=1, max=100000)], default=1234)
    userID = StringField(validators=[DataRequired(), Length(min=1)])
    alterID = StringField(validators=[DataRequired()])

    def validate_userID(self, field):
        if my_col.find({"userID": field.data}).count() > 0:
            raise ValidationError('此userID已被登记')

