#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :io_pickle.py
# @Time      :2021/10/14 20:47
# @Author    :Chen

'学习序列化'

import pickle;

d = dict(name="Bob",age=20,score=80)
#将对象转化为bytes
dbyte = pickle.dumps(d)
print(dbyte)
print(type(dbyte))

#将对象保存到文件中
f = open("pickleObj",'wb')
pickle.dump(d,f)
f.close()