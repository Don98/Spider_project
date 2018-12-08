# -*- coding:utf-8 -*-
import urllib.request

def load_page(url):
    # 发送url请求，返回url请求的静态html页面
    user_agent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    headers = {"User-Agent":user_agent}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def save_to_file(file_name,txt):
    #把返回的html请求保存到本地
    f = open(file_name,"w")
    f.write(txt)
    f.close()
    
def tieba_spider(url,start_page,end_page):
    #贴吧爬虫
    for i in range(start_page,end_page + 1):
        pn = 50 * (i-1)
        my_url = url + str(pn)
        html = load_page(my_url)
        save_to_file("第%d页.txt" % i,str(html))

if __name__ == "__main__":
    url = input("请输入贴吧的url地址:")
    start_page = int(input("请输入起始页页码:"))
    end_page = int(input("请输入终止页页码:"))
    tieba_spider(url,start_page,end_page)