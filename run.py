# -*- coding: utf-8 -*-
#! /usr/bin env python3
from getdata import get_data
from conf.setting import excel_path, out_path
from operation import to_pinyin
import time
from product import word_pinyin

if __name__ == '__main__':
    # 将excel转为txt，词语输出为拼音 来自尤
    word_pinyin(excel_path, out_path)

