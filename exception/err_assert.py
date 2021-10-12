#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :err_assert.py
# @Time      :2021/10/13 6:04
# @Author    :Chen

'使用断言调试'
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    if n==0:
        print("断言被关闭")
    return 10 / n

def main():
    foo(0)

main()