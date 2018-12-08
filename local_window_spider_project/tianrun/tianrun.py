# coding : utf-8
import requests
import re
import time
import csv

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Cookie":"cna=5Em0EkxsRFYCAXjsrqxoVX0o; thw=cn; tracknick=%5Cu5929%5Cu673A%5Cu795E%5Cu77F3%5Cu9006%5Cu5929; tg=0; miid=8401547281075913447; hng=CN%7Czh-CN%7CCNY%7C156; enc=RrUv8gPFNrcUv%2B9O2BhdkMv5f1fzlV3OYa2Dli1chv%2BwVwuBR8uJzsh9D5m4kDN99d7KWAgG5q5pbAzEK5iJGA%3D%3D; t=7f9434416bb5ca6da4f46b5a3aeb868d; lgc=%5Cu5929%5Cu673A%5Cu795E%5Cu77F3%5Cu9006%5Cu5929; uc3=vt3=F8dBzrVPUgsAMi95i5c%3D&id2=UojUAqmaSymtTA%3D%3D&nk2=r7ldDu0spwKuU%2B9y&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; _cc_=W5iHLLyFfA%3D%3D; mt=ci=-1_0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; birthday_displayed=1; swfstore=165310; cookie2=3a38395c437c7670858ce1c4ffa54053; v=0; _tb_token_=44581ebe587b; JSESSIONID=93BD78A57A94EF39F45740766B5A832F; uc1=cookie14=UoTfI8GehTfJfA%3D%3D; isg=BBcXOx1YAMIO-IVwwkeY8ddLpovNT_10KxrA6GlENeZImDfacS21DkS-_3gjQMM2",
    "Referer":"https://s.taobao.com/search?q=%E5%A4%A9%E6%B6%A6%E7%89%9B%E5%A5%B6&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
}

def get_url(response):
    all_url = re.findall(re.compile('"detail_url":"([\W\w]+?)"'),response)
    return all_url    

def get_title(response):
    # title = re.findall(re.compile('"detail_url":"([\W\w]+?)"'),response)
    title = re.findall(re.compile('"raw_title":"([\W\w]+?)"'),response)
    return title

def get_sales(response):
    sales = re.findall(re.compile('"view_sales":"([\W\w]+?)人付款"'),response)
    return sales    
    
def work(url,a):
    req = requests.get(url,headers = headers)
    response = req.content.decode('utf-8')
    # with open('1.txt','w',encoding = "utf-8") as f:
        # f.write(str(req.content.decode('utf-8')))
    title = get_title(response)
    all_url = get_url(response)
    sales = get_sales(response)
    for i in range(len(title)):
        L = [title[i],all_url[i],sales[i]]
        a.writerow(L)
    
if __name__ == "__main__":
    part1 = "https://s.taobao.com/api?_ksTS=1538046872696_298&callback=jsonp299&ajax=true&m=customized&sourceId=tb.index&q=iphone&spm=a21bo.2017.201856-taobao-item.1&s="
    part2 = "&imgfile=&initiative_id=tbindexz_20170306&bcoffset=0&commend=all&ie=utf8&rn=0c8b69fe1c8d2d74f53c4d5332841136&ssid=s5-e&search_type=item"
    with open('tianrun.csv','w',newline = "") as csvfile:
        a = csv.writer(csvfile,dialect='excel')
        L = ['title','url','sales']            
        a.writerow(L)
        n = 0
        while(True):
            url = part1 + str(n) + part2
            n += 1
            work(url,a)
            print("url" + str(n) + "爬去完毕!")
            time.sleep(5)