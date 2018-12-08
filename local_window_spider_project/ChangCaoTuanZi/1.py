#coding : utf-8
import requests
import re
import os

if __name__ == "__main__":
    req = requests.get("https://www.meipian.cn/5ltjdi6")
    reponse = str(req.content,'utf-8')
    img = re.findall(re.compile('<img show-img="[\W\w]+?" src="([\W\w]+?)">'),reponse)
    if not os.path.isdir("ChangCaoTuanZi"):
        os.mkdir("ChangCaoTuanZi")
    os.chdir("ChangCaoTuanZi")
    count = 0
    for i in img:
        html = requests.get(i)
        with open(str(count) + ".jpg" , 'wb') as f:
            f.write(html.content)
            f.flush()
            count += 1