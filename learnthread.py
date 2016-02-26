#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('process (%s) start...' % os.getpid())

#Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
	print('I am child process (%s) and my parent is %s.' % (os.getpod(),os.getppod()))
else:
	print('I (%s) just create a child process (%s)' % (os.getpid,pid))