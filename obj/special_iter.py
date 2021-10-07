#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用__iter__实现一个可以用for...in循环遍历的斐波那契数列'

__author__ = 'Chen'

class Fib:
    def __init__(self):
        self.__a,self.__b = 0,1;    # 初始化两个计数器

    def __iter__(self):
        return self;    #实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.__a,self.__b = self.__b, self.__a+self.__b;    #计算出下一个值
        if self.__a > 10000:    #退出循环条件
                raise StopIteration();
        return self.__a;



fibList = list(Fib());
print(fibList)
