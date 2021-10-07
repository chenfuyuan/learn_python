#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用__getitem__实现一个可以用下标获取元素的斐波那契数列'

__author__ = 'Chen'

class Fib:

    # getitem 参数n 可以是 整型和切片类型
    def __getitem__(self, n):

        if isinstance(n,int):
            if n < 0:
                raise IndexError("斐波那契数列为无限数列，无法使用负数索引")
            a,b = 1,1;
            for x in range(n):
                a,b = b,a+b;
            return a;

        if isinstance(n,slice):
            print(dir(n))
            start = n.start;
            stop = n.stop;
            step = n.step;
            if start is None:
                start = 0;

            a,b = 1,1;
            result = [];

            for x in range(stop):
                if start <= x:
                    if step and not (x-start)%step == 0:
                        pass;
                    else:
                        result.append(a);
                a, b = b, a + b;
            return result;



fib = Fib();


for i in range(0,11):
    print(fib[i]);

print("=============");
print(fib[:10])
print(fib[:10:4])
