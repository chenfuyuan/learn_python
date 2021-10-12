#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :err_raise.py
# @Time      :2021/10/13 6:01
# @Author    :Chen

''


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()