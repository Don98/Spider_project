import urllib.request
import requests
import re
from bs4 import BeautifulSoup
import os
import time
import random
from random import choice
from ip import ip
from us import us

def get_content(url,title,f):
    proxy = ip[random.randint(0,len(ip)-1)]
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',us[random.randint(0,len(us)-1)])]
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = str(response.read(),'gbk')
    content = re.compile('<div id="content">([\w\W]+?)</div>').findall(html)
    f.write(title)
    f.write(content[0].replace("<br/>","\n"))
    f.write("\n")

def download_content(url,filename):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    headers = {"User-Agent":user_agent}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = str(response.read(),'gb18030')   
    content = re.compile('<dd><a href="([\w\W]+?)">([\w\W]+?)</a></dd>').findall(html)
    f = open(filename + ".txt","w")
    for i in range(len(content)):
        # if i % 5 == 0 and i !=0:
            # time.sleep(random.randint(20,30))
        get_content('http://www.biquge.jp/111392_41/' + content[i][0],content[i][1],f)
        print("%s 保存 %lf" % (filename,i/len(content)*100))
    f.close()

def download_novel(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    headers = {"User-Agent":user_agent,"Referer":"http://www.biquge5200.com/"}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = str(response.read(),'gbk')
    L1 = re.compile('</span><a href="([\w\W]+?)">([\w\W]+?)</a>').findall(html)
    L2 = re.compile('《<a href="([\w\W]+?)" target="_blank">([\w\W]+?)</a>》').findall(html)
    L3 = re.compile('<span class="s2"><a href="([\w\W]+?)">([\w\W]+?)</a></span>').findall(html)
    L = L1 + L2 +L3
    # for i in L:
    download_content(L[0][0],L[0][1])

def get_html(url):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    headers = {"User-Agent":user_agent,"Referer":"https://www.baidu.com/s?wd=%E7%AC%94%E8%B6%A3%E9%98%81&rsv_spt=1&rsv_iqid=0xd5dc1f250004cb02&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=5&rsv_sug7=101"}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = str(response.read(),'gbk')
    for i in range(len(L)):
        L[i] = re.compile('<li><a href="([\w\W]+?)">([\w\W]+?)</a>)').findall(str(html))
    print()
    return L[0]

if __name__ == '__main__':
    url = "http://www.biquge.jp/1_41.html"
    content = get_html(url)
    # for i in content:
    path = os.getcwd()
    if not os.path.isdir(content[2][1]):
        os.system("mkdir %s" % content[2][1])
    os.chdir(content[2][1])
    download_novel(content[2][0])
    os.chdir(path)