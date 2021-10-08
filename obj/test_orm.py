#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_orm.py
# @Time      :2021/10/9 1:19
# @Author    :Chen

'测试orm代码'

from obj.orm import *

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    __table__ = "_User"

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')

u.save();
