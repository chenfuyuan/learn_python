#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :exception.py
# @Time      :2021/10/10 16:46
# @Author    :Chen

'测试try...except...finally...'

try:
    print("try..");
    r = 10 /0;
    print("result:",r);
except ZeroDivisionError as e:
    print("except...",e)
finally:
    print("finally...")
print("END")

print("============================")

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

print("============================")

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

print("============================")

try:
    r = 10 / 0;
except BaseException as e:
    print("except(Exception):",e)
except ZeroDivisionError as e:
    print("except(ZeroDivisionError):",e)

print("=============================")

def foo():
    r = 10 /0;
    return r;

try:
    foo();
except BaseException as e:
    print("except(Exception):", e)
except ZeroDivisionError as e:
    print("except(ZeroDivisionError):", e)