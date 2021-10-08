#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_type.py
# @Time      :2021/10/8 20:36
# @Author    :Chen

'测试type类型'

from hello import Hello;

h = Hello();
print(type(Hello))

print(type(h))

h.hello();

def fn(self,name="world"):
    print("Hello,%s"% name)

Hello1 = type("Hello1",(object,),dict(hello=fn));

h2 = Hello1();

print(type(Hello1))

print(type(h2))

h.hello();