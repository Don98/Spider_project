# -*- coding:utf-8 -*-
'''
命令行的火车票查看器
Usage:
    12306 [-gdtkz] <from> <to> <date>
    
Options:
    -h,--help 显示帮助
    -g        高铁
    -d        动车
    -t        特快
    -k        快速
    -z        直达
    
Example:
    12306 上海 北京 2018-2-25
    12306 -dg 上海 北京 2018-2-25
'''
import requests
from docopt import docopt
from stations import stations
import re
import csv
import os

header = '车次 出发站 到达站 出发时间 到达时间 历时 商务座/特等座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他'.split(' ')
L = []
# class TrainCollection:
    # header = '车次 出发站 到达站 出发时间 到达时间 历时 商务座/特等座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 其他'.split(' ')
    # def __intit__(self,available_trains,Options):
        # self.available_trains = available_trains
        # self.options = options
        
    # def trains(self):
        # for raw_train in self.available_trains:
            # train_non = raw_train['station_train_code']
    
def get_keys(value):
    t = list(stations.keys())
    for i in t:
        if stations[i] == value:
            return i
    
def cli():
    global L
    global header
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init'
    }
    url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date,from_station,to_station)
    r = requests.get(url,verify = False,headers = headers)
    available_trains = r.json()['data']['result']
    for i in range(len(available_trains)):
        L.append([0]*len(header))
        available_trains[i] = re.findall(r'\|[\w\W]+?\|\|[\w\W]+?0',available_trains[i])[0].split('|')
    for i in range(len(L)):
        L[i][0] = available_trains[i][2]
        L[i][1] = get_keys(available_trains[i][4])
        L[i][2] = get_keys(available_trains[i][5])
        L[i][3] = available_trains[i][8]
        L[i][4] = available_trains[i][9]
        L[i][5] = available_trains[i][10]
        for j in range(6,17):
            L[i][j] = available_trains[i][len(available_trains[i]) - j + 6 - 3] if available_trains[i][len(available_trains[i]) - j + 6 - 3] != '' else 0
    print("正在保存查询结果...")
    with open('from %s to %s %s.csv' % (arguments['<from>'],arguments['<to>'],arguments['<date>']),'w',newline='') as csvfile:
        a = csv.writer(csvfile,dialect='excel')
        a.writerow(header)
        for i in L:
            a.writerow(i)
    print("保存完毕")

if __name__ == '__main__':
    cli()