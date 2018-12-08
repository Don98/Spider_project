import urllib.request
import requests
import re
import time

url = "http://www.biquge.com.tw/3_3711/"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
headers = {"User-Agent":user_agent}
req = urllib.request.Request(url,headers = headers)
response = urllib.request.urlopen(req)
html = str(response.read(),"gbk")
content = re.compile('<dd><a href="([\w\W]+?)">([\w\W]+?)</a>').findall(html)
L1 = [0] * len(content)
L2 = [0] * len(content)
for i in range(len(content)):
    L1[i] = "http://www.biquge.com.tw/" + content[i][0]
    L2[i] = content[i][1]
f = open("儒道至圣.txt","w")
print(L1[0])
for i in range(len(L1)):
    req = urllib.request.Request(L1[i],headers = headers)
    response = urllib.request.urlopen(req)
    print(L2[i])
    html = str(response.read(),"gb18030")
    content = re.compile('<div id="content">([\w\W]+?)</div>').findall(html)
    try:
        f.write("%s\n" % L2[i])
        f.write(content[0].replace("<br />","").replace("&nbsp;",""))
    except:
        f.write("此章不存在")
    if i % 100 == 0:
        time.sleep(20)
    print("儒道至圣已保存 %lf" % (i / len(L1) * 100))
f.close()