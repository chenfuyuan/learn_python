#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :io_string.py
# @Time      :2021/10/14 19:16
# @Author    :Chen

'测试StringIO'

from io import StringIO;
f = StringIO()
f.write("hello")
f.write(" ")
f.write("world!")
print(f.getvalue())

f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f.readline();
    if s == "":
        break;
    print(s.strip())

