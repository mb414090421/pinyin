#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pinyin
import re

# 拼音
def to_pinyin(var_str):
    # 判断是不是str类型
    if isinstance(var_str, str):
        if var_str == 'None':
            return ""
        else:
            return pinyin.get(var_str, format='strip', delimiter="~")
    else:
        return '类型不对'

# 列表排序
'''
例如：
    ['0', '吖', '11', '']
    ['1', '吖吖', '140', '']
    ['2', '吖啶', '121', '/n']
'''
def lastchar(s):
    return int(s[-2])

# 用来存x元素，主要是用来根据词频排序
out = []
print('-' * 60)

# 打开文件
f = open('30万词库带词频.txt', 'r')
data = f.readlines()
f.close()

for x in data:
    # 正则切割
    x = re.split(r'[\n,，]', x)
    if len(x[1]) == 1:
        continue
    # 在特定的位置插入拼音
    x.insert(2, to_pinyin(x[1]))

    #加个判断是否有转音失败
    if not re.match("[a-z~]+$", x[2]):
        print(x)
        continue
    out.append(x)

#
# 根据词频排序
out = sorted(out, key=lastchar, reverse=True)

f = open('new.txt', 'w')
for i in out:
    # 重新拼接
    newx = i[1] + '\t' + i[2] + '\r\n'

    newx = newx.encode('unicode-escape')
    f.write(newx)
f.close()


