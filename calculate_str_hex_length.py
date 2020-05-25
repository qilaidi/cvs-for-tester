#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
计算String的十六进制长度
"""

import binascii, re, sys

def convert_str_to_hexstr(hex_str, group_len=2):
    hex_str = binascii.b2a_hex(hex_str.encode("gbk")).decode()
    return (" ".join([hex_str[i:i+group_len] for i in range(0, len(hex_str), group_len)]).upper())

def format_msg(msg):
    """
        Remove multiple blanks, link breaks.
    """
    msg = re.sub("\n+", " ", msg)
    msg = re.sub(" +", " ", msg)
    msg = msg.strip()
    if r" " not in msg:
        msg = " ".join([msg[i:i + 2] for i in range(0, len(msg), 2)])
    return msg.upper()

if __name__ == "__main__":
    msg_list = convert_str_to_hexstr(sys.argv[1])
    print(len(format_msg(msg_list).split()))

