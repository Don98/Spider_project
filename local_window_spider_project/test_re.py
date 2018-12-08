# -*- coding:utf-8 -*- 

import re

#创建一个正则表达式对象
pattern = re.compile('\d+\.\d+')

#提供我要匹配的源字符串
src = "3.14,121315.1,21351.2626,abc,1.23,213213"

result = pattern.findall(src)
for i in result:
    print(i)