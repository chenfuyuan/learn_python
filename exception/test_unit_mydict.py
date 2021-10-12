#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_unit_mydict.py
# @Time      :2021/10/13 6:41
# @Author    :Chen

'单元测试(MyDict)'

import unittest;
from mydict import MyDict;

class TestDict(unittest.TestCase):

    def setUp(self):
        print("启动前");

    def tearDown(self):
        print("启动后")

    def test_init(self):
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()