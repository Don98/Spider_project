#-*-coding:utf-8 -*-
import re
import urllib.request

def work(start,end):
    t=[]
    for i in range(start,end+1):
        url = "http://www.pythontip.com/coding/code_oj_case/" + str(i)
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        headers = {"User-Agent":user_agent}
        req = urllib.request.Request(url,headers = headers)
        response= urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        patt = re.compile('<p\sclass="text-center">\s+?<strong><a[\s\S]+?href="[\w\W]+?\d*?">([\w\W]+?)</a>')
        pattern = re.compile('<div class="text-info">([\w\W]+?)<br>')
        L = list(re.findall(pattern,html))
        l = ""
        for i in L:
            for j in range(len(i)):
                l += i[j]
        title = list(re.findall(patt,html))[0]
        t.append(title)
        t.append(l.replace("<pre>","").replace("<p>","").replace("</p>","").replace("<strong>","").replace("</pre>","").replace("</strong>",""))
    f = open("题目%d-%d.txt"%(start,end),"a")
    for i in t:
        f.write(i+"\n")
    f.close()
    
if __name__ == "__main__":
    start = int(input("Please input the start page :"))
    end = int(input("Please inpput the end page:"))
    work(start,end)