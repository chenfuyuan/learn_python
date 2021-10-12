#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :mydict.py
# @Time      :2021/10/13 6:54
# @Author    :Chen

'编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访'
class MyDict(dict):

    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key];
        except:
            #处理dict无对应key状况。抛出错误
            raise AttributeError(r"'MyDict' object has no attribute '%s'" % key)

    #缺少，将导致 object.key = value语句 意义为 设置一个变量为key的属性，值为value。而不是在dict中添加一个键值对
    def __setattr__(self, key, value):
        self[key]=value

