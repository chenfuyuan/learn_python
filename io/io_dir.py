#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :io_dir.py
# @Time      :2021/10/14 19:43
# @Author    :Chen

'操作文件和目录'
import os

#操作系统类型
print("操作系统类型:",os.name)

#环境变量
print("环境变量",os.environ)

#获取环境变量PATH
print("PATH:",os.environ.get("PATH"))

#获取当前路径
print("当前路径",os.path.abspath('.'))
abspath = os.path.abspath('.')

#拼接路径
#使用join方法，拼接路径。
#不要使用/直接拼接路径，各个操作系统路径拼接符不同
newDirPath = os.path.join(abspath,'newDir')
print("拼接新目录路径:",newDirPath)

#创建
#os.mkdir(newDirPath)

#删除目录
#os.rmdir(newDirPath)

#拆分路径
splitPath = os.path.split(newDirPath)
print("拆分目录路径结果:",splitPath)

#拆分后缀
splitextPath = os.path.splitext(os.path.join(abspath,'test.txt'))
print("拆分目录路径后缀结果:",splitextPath)

#修改名称
#os.rename("newDir","newDir1")

#删除文件
#os.remove("test_new_text")

#列出目录
dirList = [x for x in os.listdir('.') if os.path.isdir(x)]
print("当前目录所有文件夹:",dirList)

#列出所有的.py文件，也只需一行代码：
pyFileList =  [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print("当前目录所有的.py文件",pyFileList)