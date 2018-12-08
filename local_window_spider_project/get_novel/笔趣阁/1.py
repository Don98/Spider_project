import requests
import os
import gevent
from gevent import monkey
import random
import re
from lxml import etree
monkey.patch_all(select=False)
from urllib import parse
import time


def setDir():
    if 'Noval' not in os.listdir('./'):
        os.mkdir('./Noval')


def getNoval(url, id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '__cfduid=d820fcba1e8cf74caa407d320e0af6b5d1518500755; UM_distinctid=1618db2bfbb140-060057ff473277-4323461-e1000-1618db2bfbc1e4; ctrl_time=1; CNZZDATA1272873873=2070014299-1518497311-https%253A%252F%252Fwww.baidu.com%252F%7C1518507528; yjs_id=69163e1182ffa7d00c30fa85105b2432; jieqiVisitTime=jieqiArticlesearchTime%3D1518509603'
    }
    IPs = [
        {'HTTPS': 'https://115.237.16.200:8118'},
        {'HTTPS': 'https://42.49.119.10:8118'},
        {'HTTPS': 'http://60.174.74.40:8118'}
    ]
    IP = random.choice(IPs)
    res = requests.get(url, headers=headers, proxies=IP)
    res.encoding = 'GB18030'
    html = res.text.replace('&nbsp;', ' ')  # 替换掉这个字符 换成空格~ 意思是一样的
    page = etree.HTML(html)
    content = page.xpath('//div[@id="content"]')
    ps = page.xpath('//div[@class="bookname"]/h1')
    if len(ps) != 0:
        s = ps[0].text + '\n'
        s = s + content[0].xpath("string(.)")
        with open('./Noval/%d.txt' % id, 'w', encoding='gb18030', errors='ignore') as f:
            f.write(s)


def getContentFile(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '__cfduid=d820fcba1e8cf74caa407d320e0af6b5d1518500755; UM_distinctid=1618db2bfbb140-060057ff473277-4323461-e1000-1618db2bfbc1e4; ctrl_time=1; CNZZDATA1272873873=2070014299-1518497311-https%253A%252F%252Fwww.baidu.com%252F%7C1518507528; yjs_id=69163e1182ffa7d00c30fa85105b2432; jieqiVisitTime=jieqiArticlesearchTime%3D1518509603'
    }
    IPs = [
        {'HTTPS': 'https://115.237.16.200:8118'},
        {'HTTPS': 'https://42.49.119.10:8118'},
        {'HTTPS': 'http://60.174.74.40:8118'},
        {'HTTP':"http://10.10.1.10:3128"}, 
        {'HTTPS': "http://10.10.1.10:1080"}
    ]
    IP = random.choice(IPs)
    res = requests.get(url, headers=headers, proxies=IP)
    res.encoding = 'GB18030'
    page = etree.HTML(res.text)
    bookname = page.xpath('//div[@id="info"]/h1')[0].xpath('string(.)')
    dl = page.xpath('//div[@id="list"]/dl/dd/a')
    return list(map(lambda x: x.get('href'), dl)), bookname


def BuildGevent(baseurl):
    content, bookname = getContentFile(baseurl)  # version2
    print("1")
    steps = 200
    beginIndex, length = steps, len(content)
    count = 0
    name = "%s.txt" % bookname
    while (count - 1) * steps < length:
        WaitigList = [gevent.spawn(getNoval, content[i + count * steps], i + count * steps) for i in range(steps) if
                      i + count * steps < length]
        gevent.joinall(WaitigList)
        NovalFile = list(filter(lambda x: x[:x.index('.')].isdigit(), os.listdir('./Noval')))
        NovalFile.sort(key=lambda x: int(re.match('\d+', x).group()))
        String = ''
        for dirFile in NovalFile:
            with open('./Noval/' + dirFile, 'r', encoding='gb18030', errors='ignore') as f:
                String = String + '\n' + f.read()
            os.remove('./Noval/%s' % dirFile)
        if count == 0:
            with open('./Noval/' + name, 'w', encoding='gb18030', errors='ignore') as ff:
                ff.write(String)
        else:
            with open('./Noval/' + name, 'a', encoding='gb18030', errors='ignore') as ff:
                ff.write(String)
        count += 1


if __name__ == '__main__':
    starttime = time.time()
    setDir()
    url = 'http://www.biquge5200.com/52_52542/'
    BuildGevent(url)
    endtime = time.time()
    print("Total use time: %.6f" % (endtime - starttime))