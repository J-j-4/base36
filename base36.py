# coding=utf-8
"""
    Created by Prakash on 24/05/18
"""

__author__ = 'Prakash14'


def int_to_base36(num):
    """Converts a positive integer into a base36 string."""
    assert num >= 0
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    res = ''
    while not res or num > 0:
        num, i = divmod(num, 36)
        res = digits[i] + res
    return res


def base36_to_int(num: str):
    """
    Converts a positive base36 into a integer string.
    :param num:
    :return:
    """
    num = num.upper()
    return int(num, 36)


def nxt_value(num: str):
    """
    This for increment the base64 value
    :param num:
    """
    return int_to_base36(base36_to_int(num) + 1)


def prv_value(num: str):
    """
    This for decrement the base64 value
    :param num:
    """
    return int_to_base36(base36_to_int(num) - 1)
