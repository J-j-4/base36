# coding=utf-8
"""
    Created by Prakash on 24/05/18
"""
import unittest
import base36

__author__ = 'Prakash14'


class TestBase(unittest.TestCase):

    def test_int_to_base36(self):
        assert base36.int_to_base36(10) == 'A'
        assert base36.int_to_base36(13) == 'D'
        assert base36.int_to_base36(35) == 'Z'

    def test_base36_to_int(self):
        assert base36.base36_to_int('A') == 10
        assert base36.base36_to_int('D') == 13
        assert base36.base36_to_int('Z') == 35

    def test_nxt_value(self):
        assert base36.nxt_value("ASEZ") == 'ASF0'
        assert base36.nxt_value("ZEWS") == 'ZEWT'

    def test_prv_value(self):
        assert base36.prv_value("ASF0") == 'ASEZ'
        assert base36.prv_value("ZEWT") == 'ZEWS'

    def test_sequence_number(self):
        for i in range(100, 100000):
            base_36 = base36.int_to_base36(i)
            print('%s : %s' % (i, base_36))
            assert i == base36.base36_to_int(base_36)
