# -*- coding:utf-8 -*-
import requests
import re
import os
import random
from ip import ip
from us import us
import urllib
import urllib.request

book_type = []
book_start = []

def download_chapter(url,title,f):
    response = requests.get(url)
    content = re.compile('<div id="content">([\w\W]+?)</div>').findall(response.text)
    f.write(title)
    f.write("\n")
    f.write(content[0].replace("&nbsp;","").replace("<br/>","\n").replace("<br />","\n"))
    f.write("\n")

def download_novel(url,bookname,auther):
    if random.randint(1,10) == 5:
            proxy = ip[random.randint(0,len(ip)-1)]
            proxy_support = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(proxy_support)
            opener.addheaders = [('User-Agent',us[random.randint(0,len(us)-1)])]
            urllib.request.install_opener(opener)
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
    else:
        response = requests.get(url)
        content = re.compile('<dd><a href="([\w\W]+?)">([\w\W]+?)</a></dd>').findall(response.text)
    f = open("%s(%s).txt"%(bookname,auther),"w")
    for i in content:
        download_chapter(url + i[0],i[1],f)
    f.close()
    print("小说%s(%s)保存完毕"%(bookname,auther))

def get_url(url):
    response = requests.get(url)
    global book_type
    book_types = re.compile('<h2>([\w\W]+?)</h2>[\w\W]+?<li><a href="([\w\W]+?)">([\w\W]+?)</a>/([\w\W]+?)</li>').findall(response.text)
    bookInfos= re.compile('<li><a href="([\w\W]+?)">([\w\W]+?)</a>/([\w\W]+?)</li>').findall(response.text)
    for i in book_types:
        book_type.append(i[0])
        book_start.append(i[2])
    return bookInfos #url , bookname , auther
    
if __name__ == '__main__':
    url = "http://www.biquge.jp/1_11.html"
    bookInfos = get_url(url)
    t = 0
    intial_path = os.getcwd()
    del bookInfos[0]
    for i in bookInfos:
        if t % 1000 == 0:
            os.chdir(intial_path)
            if not os.path.isdir(book_type[(t - t%1000)//1000]):
                os.system("mkdir %s" % book_type[(t - t%1000)//1000])
                print(count)
            print(book_type[(t - t%1000)//1000])
            os.chdir(book_type[(t - t%1000)//1000])
            download_novel(i[0],i[1],i[2])
        else:
            download_novel(i[0],i[1],i[2])
        t += 1