#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_enum.py
# @Time      :2021/10/8 19:35
# @Author    :Chen

'测试枚举类'

__author__ = 'Chen'

from enum import Enum, unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


for name, member in Month.__members__.items():
    print("%s:%s" % (name, member))


# 助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0;  # Sun的value被设定为0
    Mon = 1;
    #Mon = 2;
    #ValueError: duplicate values found in <enum 'Weekday'>: Tue -> Mon
    Tue = 2;
    Wed = 3;
    Thu = 4;
    Fri = 5;
    Sat = 6;

for name,member in Weekday.__members__.items():
    print("%s:%s" % (name, member))