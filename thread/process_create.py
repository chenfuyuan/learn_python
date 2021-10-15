#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :process_create.py
# @Time      :2021/10/15 21:33
# @Author    :Chen

''
import os;
# Only works on Unix/Linux/Mac:
#pid = os.fork()
#print("pid=",pid)

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')