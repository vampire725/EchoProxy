# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/18 0018 10:09
# @Author   : Gpp
# @File     : register.py
from flask import render_template, request, redirect, url_for

from app.forms.register import RegisterForm
from app.models.register import Register
from app.models.base import db
from . import web


@web.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        register_table = Register()
        register_table.set_attrs(form.data)
        db.session.add(register_table)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login')
def login():
    return 'login'
