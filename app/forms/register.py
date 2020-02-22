# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 11:45
# @Author   : Gpp
# @File     : register_table.py
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from app.models.register_table import Register


class RegisterForm(Form):
    ip = StringField(validators=[DataRequired(), Length(min=4, max=25, message="IP地址不和规范")])
    port = IntegerField(validators=[NumberRange(min=1, max=100000)], default=1234)
    userID = StringField(validators=[DataRequired(), Length(min=1)])
    alterID = StringField(validators=[DataRequired()])

    def validate_userID(self, field):
        if Register.query.filter_by(userID=field.data).first():
            raise ValidationError('此userID已被登记')

