# -*- coding:utf-8 -*-

import scrapy
from novel_spider.items import NovelItem
import urllib.request
import os
import re

L = []

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def make(part,title):
    title = validateTitle(title)
    f = open(r'%s.txt' % title,"w")
    url = "http://www.biquge.jp/111392_41/" + str(part)
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    headers = {"User-Agent":user_agent}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = str(response.read(),'gbk')
    pattern = re.compile(r'<div id="content">(.*?)</div>',re.S)
    item_list = pattern.findall(html)[0].replace("&nbsp","").replace("<br/>","")
    f.write(item_list)
    global L
    L.append(title)
    L.append(item_list)
    f.close()
class novelSpider(scrapy.spiders.Spider):
    name = "get_novel"
    start_urls = ["http://www.biquge.jp/111392_41/"]
    

    
    def parse(self,response):
        # f = open("novel.txt","w")
        # f.write(str(response.body))
        # f.close()
        items = []
        it = response.xpath('//dd/a/text()').extract()
        html = response.xpath('//dd//a/@href').extract()
        if not os.path.isdir("雪鹰领主"):
            os.mkdir("雪鹰领主")
        os.chdir("雪鹰领主")
        f = open("章名.txt","a")
        count = 0
        for i in range(len(it)):
            item = NovelItem()
            item["title"] = it[i]
            item["body"] = html[i]
            make(html[i],it[i])
            print("第%d章储存完成"%(i+1))
            items.append(item)
            count += 1
            f.write(it[i]+'\n'+html[i]+'\n')
        a = open("雪鹰领主全文.txt","a")
        global L
        for i in range(len(L)):
            a.write(L[i]+"\n")
        print("全文储存完成")
        f.write(str(count))
        f.close()
        return items
        # www.biquge.jp/111392_41/5470505.html
        # http://www.biquge.jp/111392_41/5470506.html