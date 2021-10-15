#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :serialize_json.py
# @Time      :2021/10/15 20:21
# @Author    :Chen

'序列化json'

import json

#将内置数据类型转化为str
d = dict(name="Bob", age=20, score=80)
dumpDict = json.dumps(d)
print("dumpDict = ", dumpDict)
# <class 'str'>
print("dumpDict.type = ", type(dumpDict))

#将内置数据类型存储到文件中
f = open("jsonObj", "w")
json.dump(d, f)


#Object to JSON
class Student(object):
    def __init__(self, name, age, score):
        self.name = name;
        self.age = age;
        self.score = score;

    def __str__(self):
        return "<name:%s,age:%s,score:%s>" % (self.name, self.age, self.score)


f_s = open("jsonObj_student","w")
s = Student("Simon", 20, 80)
#Object of type Student is not JSON serializable
#json.dump(s,f_s)

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
#json.dump(s,f_s,default=student2dict)

#通用的obj转化为dict对象
def obj2Dict(obj):
    return obj.__dict__;
json.dump(s, f_s, default=obj2Dict)


#将对象转化为str对象
jsonStr = json.dumps(s,default=obj2Dict)
print("jsonStr = ",type(jsonStr))

#将dict对象转化为Student
def dict2Student(kw):
    return Student(**kw)
#object_hook 对象_挂钩 传入一个函数，用于把 json对象转化为对应对象
jsonStudent = json.loads(jsonStr,object_hook=dict2Student)
print("jsonStudent = ",jsonStudent)