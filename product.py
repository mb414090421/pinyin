# -*- coding: utf-8 -*-
#! /usr/bin env python3
from getdata import get_data
from conf.setting import excel_path, out_path
from operation import to_pinyin
import time

def word_pinyin(path, out_path):
    '''
            get_data返回的是一个字典，要获取数据就要加['data'],['0']表示第一张表，其中必须是str,不是下标
            例如data = [['打字频次', '词语'],
                        [146977.0, '提拉'],
                        [342048.0, '流逝'],
                        [183593.0, '周一'],
                        [149140.0, '一课'],
                        [141673.0, '救'],
                        [116314.0, '随'],
                        [96374.0, '下集']]
    '''
    localtime = time.strftime("%Y-%m-%d", time.localtime())
    out_path = out_path + '%s.txt' % localtime
    with open(out_path, 'w') as f:
        data = get_data(path)['data']['0']
        data = data[1::]
        for x in data:
        #     # x = ['打字频次', '词语']
            pinyin = to_pinyin(x[1])
            row = ('%s' + '\t' + '%s' + '\n') % (x[1],pinyin)
            f.write(row)
        f.close()
        print('ok')

