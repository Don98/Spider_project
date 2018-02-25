import urllib.request
import re
import os

def get_content(part,title,f):
    url = "http://www.neihanpa.com/article/" + str(part)
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    }
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = str(response.read(),'utf-8')
    content = re.compile('<p>([\w\W]+?)</p>').findall(html)
    del content[len(content)-1]
    for i in content:
        f.write(i.replace("&nbsp;","").replace("&hellip;","").replace("&ldquo;","").replace("&rdquo;",""))
    
def download_page(url,satrt,end,f):
    for i in range(satrt,end+1):
        if start == 1:
            url = url
        else:
            url = url + "index_" + str(i) + ".html"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = str(response.read(),'utf-8')
        content = re.compile('<h3><a href="/article/([\w\W]+?)" class="title" title="([\w\W]+?)">').findall(html)
        for j in content:
            get_content(j[0],j[1],f)
        print("第%d保存完毕！" % i)

    
if __name__ == '__main__':
    url = "http://www.neihanpa.com/article/"
    start = int(input("请输入起始页："))
    end = int(input("请输入终止页："))
    f = open('内涵段子.txt',"w")
    download_page(url,start,end,f)
    f.close()
    print("保存完毕！")
