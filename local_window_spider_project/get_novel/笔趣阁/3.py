import urllib.request
import re
url = "http://www.xicidaili.com/"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
headers = {"User-Agent":user_agent}
req = urllib.request.Request(url,headers = headers)
response = urllib.request.urlopen(req)
html = str(response.read(),'utf-8')   
ip = re.compile('<td class="country">[\w\W]+?<td>([\w\W]+?)</td>').findall(html)
f = open("ip.py","w")
f.write("[")
print(len(ip))
for i in range(len(ip)):
    print(i)
    if i % 2 ==0:
        f.write('{"%s":"%s"},' % (ip[i+1],ip[i]))
f.write("]")
f.close()
        