#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :process_subprocess.py
# @Time      :2021/10/15 22:28
# @Author    :Chen

' subprocess'
import subprocess;

#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup', 'www.python.org'])
#print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)