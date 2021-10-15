#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :io_pickle.py
# @Time      :2021/10/14 20:47
# @Author    :Chen

'学习序列化'

import pickle;

d = dict(name="Bob",age=20,score=80)
f = open("pickleObj",'wb')
pickle.dump(d,f)
