#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用__getattr__，编写一个API URL生成器'

__author__ = 'Chen'

class Chain:

    def __init__(self,path=""):
        self.__path = path

    def __getattr__(self, path):
        return Chain("%s/%s"%(self.__path,path))



    def __str__(self):
        return self.__path

    __repr__ = __str__

print(Chain().status.user.timeline.list)