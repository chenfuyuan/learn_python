#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_metaclass.py
# @Time      :2021/10/9 0:09
# @Author    :Chen

'测试metaclass'

class ListMataclass(type):
    def __new__(cls,name,bases,attrs):
        print("mataclass__new__")
        attrs["add"] = lambda self,value: self.append(value)
        return type.__new__(cls,name,bases,attrs)


    def __init__(self,*args,**kwargs):
        print("mataclass__init__")
        return super().__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("mataclass__call__")
        return super().__call__(*args,**kwargs)


class MyList(list,metaclass=ListMataclass):
    print("out print")

    def __new__(cls, *args, **kwargs):
        print("MyList__new__")
        return super().__new__(cls, *args,**kwargs)

    def __init__(self):
        print("MyList__init__")

    def __call__(self, *args, **kwargs):
        print("MyList__call__")

a = MyList()
a.add("sss")
print(a)
