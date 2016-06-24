#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999....')
