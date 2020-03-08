# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/2 0002 22:15
# @Author   : Gpp
# @File     : host_proxy.py
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Host(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    operator = Column(String(30))
    local = Column(String(50))
    bandwidth = Column(Integer)
    flow_limit = Column(Float)
    ip = Column(String(50), nullable=False, unique=True)
    ssh_port = Column(Integer)
    ssh_user = Column(String(30))
    ssh_pass = Column(String(30))


class ProxyVmess(Base):
    id = Column(String(30), primary_key=True, unique=True, nullable=False)
    host_id = Column(Integer, ForeignKey('host.id'))
    proxy_id = Column(String(100))
    v = Column(String(30))
    ps = Column(String(30))
    add = Column(String(30))
    port = Column(String(30))
    aid = Column(String(30))
    net = Column(String(30))
    type = Column(String(30))
    host = Column(String(30))
    path = Column(String(30))
    tls = Column(String(30))
    proxy_type = Column(String(30), nullable=False)
    is_share = Column(String(30), default=True)
    host_information = relationship('Host', backref="vmess_of_host")


class ProxySs(Base):
    id = Column(String(30), primary_key=True, unique=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    add = Column(String(30))
    port = Column(String(30))
    secret = Column(String(30))
    password = Column(String(30))
    alias = Column(String(30))
    proxy_type = Column(String(30), nullable=False)
    is_share = Column(String(30), default=True)
    host_information = relationship('Host', backref="ss_of_host")
