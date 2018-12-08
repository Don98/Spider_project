# -*- coding:utf-8 -*- 
import requests
import re
from pprint import pprint

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9047"
response = requests.get(url,verify=False)
stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
# print(stations)
pprint(dict(stations),indent = 4)