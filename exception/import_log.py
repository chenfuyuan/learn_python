#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :import_log.py
# @Time      :2021/10/13 5:55
# @Author    :Chen

'将异常写入log中'
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')