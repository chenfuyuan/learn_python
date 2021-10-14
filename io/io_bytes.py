#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :io_bytes.py
# @Time      :2021/10/14 19:29
# @Author    :Chen

'使用 BytesIO'
from io import BytesIO;
f = BytesIO();
f.write("中文".encode("utf-8"))

print(f.getvalue())
