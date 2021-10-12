#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :debug_logging.py
# @Time      :2021/10/13 6:16
# @Author    :Chen

'使用logging 来调试'

import logging
#默认等级为WARNING
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('info:n = %d' % n)
logging.debug('debug:n = %d' % n)
logging.warning('warning:n = %d' % n)
logging.error('error:n = %d' % n)
print(10 / n)


