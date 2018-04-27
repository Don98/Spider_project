’‘’
Author :Don
‘’‘
# -*- coding:utf-8 -*-
import requests
import re
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
import csv
import os
import time

def get_url(i):
    url =" https://baike.baidu.com/api/wikiui/gethistorylist?tk=a5d8192f25053e8a95d8a752b0ac848e&lemmaId=6141470&from=" + str(i) + "&count=1&size=26"
    headers = {"User-Agent":"User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0","Cookie":"BAIDUID=46B863A870610364D1DDABB655F9B541:FG=1; BIDUPSID=46B863A870610364D1DDABB655F9B541; PSTM=1517810654; __cfduid=d23ee34b3a2059e8b72fc9182128c4ed21519923179; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1460_21092_20928; PSINO=7; pgv_pvi=7699130368; pgv_si=s5361468416; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1524544453,1524749269,1524818240,1524819638; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1524819638"
    ,"Referer":"https://baike.baidu.com/historylist/%E4%B8%87%E7%A7%91/6141470"}
    response = requests.get(url,headers = headers)
    req = response.content.decode('utf-8')
    time1 = re.findall(re.compile('"createTime":([\d\D]*?),'),req)
    L = []
    for i in time1:
        st = time.localtime(int(i))
        time2 = time.strftime('%Y-%m-%d %H:%M:%S', st)
        L.append(time2)
    return L
    
def draw_picture(x01,y0):
    plt.figure(figsize=(72,36))
    plt.plot(x01,y0)
    plt.show()
    
if __name__ == '__main__':
    L = []
    for i in range(1,12):
        L += get_url(i)
    x1 = [datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in L]
    x0 = list(map(lambda x: str(x), pd.date_range('1/7/2006','26/4/2018')))
    y0 = [0] * len(x0)
    x01 = list(map(lambda x : datetime.strptime(x[:-9], '%Y-%m-%d'),x0))
    for i in x1:
        y0[(i - x01[0]).days] += 1
    # draw_picture(x01,y0)
    count = 0
    with open('万科1.csv','w',newline='') as csvfile:
        a = csv.writer(csvfile,dialect='excel')
        for i in range(len(x0)):
            if y0[i] != 0:
                # print(x1[len(x1) - count - 1] , x0[i-1] , x0[i])
                a.writerow([x1[len(x1) - count - 1],y0[i]])
                count += y0[i]
            else:
                a.writerow([x0[i],y0[i]])
    os.system('万科1.csv')
