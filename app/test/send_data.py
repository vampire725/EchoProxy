# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/25 0025 10:52
# @Author   : Gpp
# @File     : send_data.py

import requests

example = {
    "v": "2",
    "ps": "GCP-TW",
    "add": "34.80.52.191",
    "port": "45461",
    "id": "ec6a267e-987d-44a8-aff5-fd646e9b6d87",
    "aid": "233",
    "net": "tcp",
    "type": "none",
    "host": "",
    "path": "",
    "tls": "",
}
example2 = {
    "add": "34.80.60.73",
    "port": 35535,
    "secret": "aes-256-cfb",
    "password": "t14RB2u6D5dA",
}
example3 = {
    "v": "2",
    "ps": "BWG-LA",
    "add": "65.49.212.111",
    "port": "62860",
    "id": "523f96fd-a480-4b13-919e-ddd54dee3d71",
    "aid": "233",
    "net": "tcp",
    "type": "none",
    "host": "",
    "path": "",
    "tls": "",
}

one_encrypt_data = {"data": [
    {"id": "sdf", "encrypt_data": "vmess://eyd2JzogJzInLCAncHMnOiAnR0NQLVRXJywgJ2F"
                                  "kZCc6ICczNC44MC41Mi4xOTEnLCAncG9ydCc6ICc0NTQ2MS"
                                  "csICdpZCc6ICdlYzZhMjY3ZS05ODdkLTQ0YTgtYWZmNS1mZ"
                                  "DY0NmU5YjZkODcnLCAnYWlkJzogJzIzMycsICduZXQnOiAn"
                                  "dGNwJywgJ3R5cGUnOiAnbm9uZScsICdob3N0JzogJycsICdw"
                                  "YXRoJzogJycsICd0bHMnOiAnJ30=\n"},
    {"id": "dd", "encrypt_data": "ss://YWVzLTI1Ni1jZmI6dDE0UkIydTZENWRBQDM0LjgwLjYwLjczOjM1NTM1\n"},
    {"id": "cc", "encrypt_data": "vmess://eyd2JzogJzInLCAncHMnOiAnQldHLUxBJywgJ2FkZCc6ICc2NS40OS4yMTIuMTExJywgJ3BvcnQnOiAnNjI4NjAnLCAnaWQnOiAnNTIzZjk2ZmQtYTQ4MC00YjEzLTkxOWUtZGRkNTRkZWUzZDcxJywgJ2FpZCc6ICcyMzMnLCAnbmV0JzogJ3RjcCcsICd0eXBlJzogJ25vbmUnLCAnaG9zdCc6ICcnLCAncGF0aCc6ICcnLCAndGxzJzogJyd9\n"}
]}
# r = requests.post("http://127.0.0.1:757/register", json=example3)
h = requests.post("http://127.0.0.1:757//load/file", json=one_encrypt_data)