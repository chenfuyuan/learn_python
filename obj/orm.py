#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :orm.py
# @Time      :2021/10/9 1:08
# @Author    :Chen

'编写简易orm框架'


# 字段
class Field(object):
    def __init__(self,name,colum_type):
        self.name = name;
        self.colum_type = colum_type;

    def __str__(self):
        return "<%s:%s>"%(self.__class__.__name__,self.name)

# 字符串字段
class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,"varchar(100)")

# 整型字段
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,"bigint")

# Model元组
class ModelMetaClass(type):
    def __new__(cls,name,bases,attrs):
        if name == "Model":
            return type.__new__(cls,name,bases,attrs)

        print("Found Model is %s"%name);
        print("attr=",attrs)
        #构建 字段映射
        mappings = dict();
        for k,v in attrs.items():
            if isinstance(v,Field):
                mappings[k]=v;
        #删除attrs中的字段信息，避免冲突
        for k in mappings.keys():
            attrs.pop(k);

        attrs['__mappings__'] = mappings;

        talbeName = attrs.get("__table__")
        print(talbeName)
        if not isinstance(talbeName,str):    #如果未设置表名或者表名不为字符串类型,表名将跟类名同名
            attrs['__table__'] = name;

        return type.__new__(cls,name,bases,attrs);

# 基准Model
class Model(dict,metaclass=ModelMetaClass):



    def __init__(self,**kw):
        #调用dict的__init__方法将kw中的参数，写入dict中
        super(Model,self).__init__(**kw);

    def __getattr__(self, key):
        result = self[key];
        if result:
            return result;
        else:
            print("查询不到对应映射")
            return None;

    def __setattr__(self, key, value):
        self[key] = value;

    def save(self):
        field = [];
        params = [];
        args = [];

        for k,v in self.__mappings__.items():
            field.append(k);
            params.append("?");
            args.append(getattr(self,k,None));

        sql = "insert into %s (%s) values (%s)"%(self.__table__,','.join(field),','.join(params));

        print("SQL:%s"%sql);
        print("args:%s"%str(args))