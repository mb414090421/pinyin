#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pinyin
import re


# 将词转为拼音（词语 转换为 ci~yu）

def to_pinyin(var_str):
    # 判断是不是str类型
    if isinstance(var_str, str):
        if var_str == 'None':
            return ""
        else:
            return pinyin.get(var_str, format='strip', delimiter="~")
    else:
        return '类型不对'