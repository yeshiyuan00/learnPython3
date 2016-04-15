#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列：
result_queue = queue.Queue()

#从BaseManager继承的QueueManager:
class QueueManage(BaseManager):
	pass

# 把两个Queue都注册到网络上,callable参数关联了Queue对象