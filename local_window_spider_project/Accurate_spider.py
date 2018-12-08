# -*- coding:utf-8 -*-
import urllib.request
import re
import os

class Spider:
    '''
        段子吧的 一个 爬虫类
    '''
    def __init__(self):
        self.enable = True
        self.page = 1
        
    def load_page(self,page):
        '''
            发送url请求
            返回url请求的静态的html的页面
        '''
        url = "http://www.neihanpa.com/article/list_5_" + str(page) + ".html"
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        headers = {"User-Agent":user_agent}
        req = urllib.request.Request(url,headers = headers)
        response = urllib.request.urlopen(req)
        html = str(response.read(),'gbk')
        #new_html = html.decode("gb2312").encode("gbk")
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        item_list = pattern.findall(html)
        return item_list
        
    def deal_one_page(self,item_list,page):
        '''
            处理一页的数据
        '''
        print("正在存储第%d页的段子\n" % page)
        for item in item_list:
            item.replace("<p>","").replace("<br />","").replace("</p>","").replace("&ldquo;","").replace("&rdquo;","").replace("&hellip;","")
            self.save_to_file(item)
            print(".",end="")
        print("\n第%d页的段子存储完毕\n" % page)
    
    
    def save_to_file(self,txt):
        f = open("1.txt","a")
        f.write(txt)
        f.close()
    
    def do_work(self):
        '''
            交互
        '''
        while self.enable:
            print("按回车继续")
            print("输入quit退出")
            command = input()
            if(command == "quit"):
                self.enable = False
                break;
            item_list = self.load_page(self.page)
            self.deal_one_page(item_list,self.page)
            self.page += 1
        
if __name__ == "__main__":
    mySpider = Spider()
    mySpider.do_work()
    os.system("notepad++ 1.txt")