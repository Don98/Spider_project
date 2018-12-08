import re 
import requests
import os
import json

def validateName(name):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_name = re.sub(rstr, "_", name)  # 替换为下划线
    return new_name

def load_picture(url,i,k):
    if k:
        url = "http://www.yggk.net" + url
    try:
        html = requests.get(url)
        with open(str(i) + '.jpg' , 'wb') as f:
            f.write(html.content)
            f.flush()            
    except:
        pass
        
def smaller(url,i):
    response = requests.get(url)
    req = response.content.decode('gb2312',"ignore")
    do_smaller = re.findall(re.compile('<div class="big-pic">([\w\W]+?)</div>'),str(req))
    picture = re.findall(re.compile('''<img alt="" src="([\w\W]+?)" />'''),str(do_smaller))
    k = 1
    if len(picture) == 0:
        picture = re.findall(re.compile('''src="([\w\W]+?)"'''),str(do_smaller))
        k = 0
    if len(picture) != 0:
        load_picture(picture[0],i,k)
        
def to_do_more(picture):
    response = requests.get(picture)
    req = response.content.decode('gb2312',"ignore")
    num = re.findall(re.compile('<a>([\w\W]+?)</a>'),str(req))
    num = int(num[0][1:-3])
    for i in range(num):
        if i == 0:
            url = picture + "index.html"
            smaller(url,i)
        else:
            url = picture + "index_" + str(i + 1) + ".html"
            smaller(url,i)
        
def download_pictures(url):
    response = requests.get(url)
    req = response.content.decode('gbk',"ignore")
    place = re.findall(re.compile('<ul class="product01 show">([\w\W]+?)</ul>'),str(req))
    smaller_place =re.findall(re.compile("<li>([\w\W]+?)</li>"),place[0])    
    if not os.path.isdir('xiaohua_picture'):
        os.mkdir('xiaohua_picture')
    os.chdir('xiaohua_picture')
    for i in smaller_place:
    # i = smaller_place[6]
        picture = re.findall(re.compile('''<a href="([\w\W]+?)" class'''),i)[0]
        name = re.findall(re.compile("<p>([\w\W]+?)</p>"),i)[0]
        path = os.getcwd()
        name = validateName(name)
        if not os.path.isdir(name):
            os.mkdir(name)
        os.chdir(name)
        to_do_more(picture)
        os.chdir(path)

              
if __name__ == '__main__':
    url = "http://www.yggk.net/xiaohua/xiaohua/list"
    for i in range(1,4):
        url = url + str(i) + '.html'
        download_pictures(url)