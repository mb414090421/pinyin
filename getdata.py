# -*- coding: utf-8 -*-
#! /usr/bin env python3
import xlrd
import csv
import chardet

def get_data(path):
    udict = {}
    udict['data'] = {}
    udict['nrows'] = {}
    udict['ncols'] = {}
    # TODO 一个excel里要获取多张表
    # excel文件
    if path[-1] == 'x':
        data = xlrd.open_workbook(path)
        sheets_nums = len(data.sheet_names())
        udict['num'] = sheets_nums

        for x in (0,(sheets_nums-1)):
            # 第几张表
            table = data.sheets()[x]
            # 行数
            nrows = table.nrows
            # 列数
            ncols = table.ncols
            # 转换为str
            x = '%s' % x
            set = []
            for i in range(nrows):  # 循环打印每行的数据
                set.append(table.row_values(i))
            udict['data'][x] = set
            udict['nrows'][x] = nrows
            udict['ncols'][x] = ncols
        return udict