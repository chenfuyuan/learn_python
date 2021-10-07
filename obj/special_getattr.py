#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试__getattr__方法'

__author__ = 'Chen'

class Student(object):

    def __init__(self,name):
        self.__name = name;

    def __getattr__(self, attr):
        if attr=='score':
            return 90;
        if attr=='age':
            return lambda :25;
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

vito = Student('vito');
print(vito.score)
print(vito.age())
print(vito.addr)

