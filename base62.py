# coding=utf-8
"""
    Created by Prakash on 24/05/18
"""

__author__ = 'Prakash14'


def int_to_base62(num: int):
    """Converts a positive integer into a base36 string."""
    assert num >= 0
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    res = ''
    while not res or num > 0:
        num, i = divmod(num, 62)
        res = digits[i] + res
    return res