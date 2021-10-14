#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_open.py
# @Time      :2021/10/14 0:09
# @Author    :Chen

'测试open()函数'


with open("test.txt",'r') as f:
    print(f.read())

f = open("test.txt",'r')
print("================readlines==============")
for x in f.readlines():
    print(x.strip())

f = open("test.txt",'r')
print("================while-readline===============")
while True:
    s = f.readline()
    if s =="":
        break
    print(s.strip())

print("================readByte================")
fb = open("test_chinese.txt","rb")
for x in fb.readlines():
    print(x.strip())

print("================readChinese=============")
fc = open("test_chinese.txt",'r',encoding='utf-8',errors='ignore')
for x in fc.readlines():
    print(x.strip())

fw = open("test_write.txt","a",encoding="utf-8")
fw.write("hello world")
fw.write("测试文档")
fw.close()

print("===")
fc = open("test_chinese.txt",'r',encoding='utf-8',errors='ignore')
print(fc.read(3))