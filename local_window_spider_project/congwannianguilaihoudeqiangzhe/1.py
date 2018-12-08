#coding: utf-8
import requests
import re
import time

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

def down_one(url,name):
    req = requests.get(url)
    html = req.content.decode("utf-8")
    L = re.findall(re.compile('<div id="content" deep="3">[\w\W]+?</p>([\w\W]+?)<div align="center">[\w\W]+?</div>'),html)
    # print(L)
    L[0] = L[0].replace("<br/><br/>","\n")
    L[0] = L[0].replace("&nbsp;"," ")
    # print(L[0])
    name = validateTitle(name)
    with open(name + ".txt" ,"w") as f:
        f.write(L[0])
    
def concat(names,index):
    with open("从万年后归来的强者.txt","a") as f:
        for i in range(index - 100,index):
            name = validateTitle(names[i])
            with open(names[i] + ".txt","r") as f1:
                data = f1.readlines()
            for j in data:
                f.write(j)
            
    
def chapter(url):
    req = requests.get(url)
    html = req.content.decode("utf-8")
    L = re.findall(re.compile('<dd> <a style="" href="([\w\W]+?)">[\w\W]+?</a></dd>'),html)
    names = re.findall(re.compile('<dd> <a style="" href="[\w\W]+?">([\w\W]+?)</a></dd>'),html)
    print(html)
    for i in range(422):
        L.pop(0)
        names.pop(0)
    for i in range(len(L)):
        print(names[i])
        print(L[i])
        down_one("https://www.166xs.cc/" + L[i],names[i])
        time.sleep(50)
        print("已下载" + str((i+1) / len(L) * 100) + "%")
        if((i + 1) % 100 == 0):
            concat(names,i+1)

if __name__ == "__main__":
    chapter("https://www.166xs.cc/xiaoshuo/81994/")