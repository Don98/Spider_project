import requests
import re
url = "https://wenku.baidu.com/view/14d574c5783e0912a3162a98.html"
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

# <p class="reader-word-layer reader-word-s1-3" style="width:2485px;height:225px;line-height:225px;top:3175px;left:3775px;z-index:232;false">马克思主义基本原理概论
# </p>
response = requests.get(url,headers = headers)
req = response.content.decode('utf-8','ignore')
content = re.findall(re.compile('''<p([\w\W]+?)</p>'''),str(req))
with open('1.txt','w',encoding = 'utf-8') as f:
    f.write(content[0])