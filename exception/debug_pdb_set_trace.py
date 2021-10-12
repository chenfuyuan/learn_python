#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :debug_pdb_set_trace.py
# @Time      :2021/10/13 6:34
# @Author    :Chen

'使用pdb进行断点调试'
import pdb;
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
