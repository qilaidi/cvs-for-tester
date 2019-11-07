# -*- encoding: utf-8 -*-
"""
compare everything you want, if not, contact me.
"""
'''
Created on Jun 12, 2018

'''
false = 1
true = 0
null = 0


def dict_changeable_key_handle(dict_msg):
    """
    remove dict key that no need to compare
    """
    ignore_compare_list = ["time", "time_stamp", "create_time", "createtime", "updatetime",
                           "start_time"]
    for item in ignore_compare_list:
        if item in dict_msg.keys():
            del dict_msg[item]
    return dict_msg


def compare_dict(expect_dict_data, actual_dict_data):
    """
    Compare two dict, except some changeable keys.
    Return True when equal, else return False
    """
    expect_msg = dict_changeable_key_handle(expect_dict_data)
    actual_msg = dict_changeable_key_handle(actual_dict_data)
    result = expect_msg == actual_msg
    different_key_list = []
    common_key_list = []
    if not result:
        for k in expect_msg.keys():
            if k in actual_msg.keys():
                if actual_msg[k] != expect_msg[k]:
                    different_key_list.append(k)
                    del actual_msg[k]
                else:
                    common_key_list.append(k)
                    del actual_msg[k]
            else:
                different_key_list.append(k)
        for k in actual_msg.keys():
            if k not in different_key_list:
                different_key_list.append(k)
        different_dict = {}
        for key in different_key_list:
            if key in expect_msg.keys():
                if 'expect' not in different_dict.keys():
                    different_dict['expect'] = {}
                different_dict['expect'][key] = expect_msg[key]
            if key in actual_data.keys():
                if 'actual' not in different_dict.keys():
                    different_dict['actual'] = {}
                different_dict['actual'][key] = actual_data[key]
        print("different=%r\ncommon=%r" % (different_dict, common_key_list))
    return result


def compare_list(expect_list_data, actual_list_data):
    """
    Compare if two list is equal
    """
    if len(expect_list_data) != len(actual_list_data):
        return "Length is different"
    for index in range(len(expect_list_data)):
        result = compare(expect_list_data[index], actual_list_data[index])
    return result


def compare_str(expect_str_data, actual_str_data):
    """
    Compare if two str is equal
    """
    return expect_str_data == actual_str_data


def compare(expect_compare_data, actual_compare_data):
    """Compare any two"""
    if type(expect_compare_data) != type(actual_compare_data):
        return "Different data type can not compare."
    elif isinstance(expect_compare_data, list):
        return compare_list(expect_compare_data, actual_compare_data)
    elif isinstance(expect_compare_data, str):
        return compare_str(expect_compare_data, actual_compare_data)
    elif isinstance(expect_compare_data, dict):
        return compare_dict(expect_compare_data, actual_compare_data)
    else:
        raise NotImplementedError("Contact me to cover this type.")


expect_data = [{"one": 1, "two": 1572260612000, "three": 1572278399000, "four": "000000",
                "five": 0, "six": 2, "seven": 2, "eight": 403109120, "nine": null}]

actual_data = [{"one":1,"two":1572260612000,"three":1572278399000,"four":"000000","five":0,"six":2,"seven":2,"eight":403109120,"nine":null}]

print(compare(expect_data, actual_data))
