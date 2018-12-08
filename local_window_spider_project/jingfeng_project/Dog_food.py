#-*-coding:utf-8-*-

import re
from urllib.request import urlopen
from urllib.parse import quote

def get_prod(keyword):
    # url = "https://search.jd.com/Search?keyword = " + quote(keyword) + "&enc=utf-8"
    url = "https://search.jd.com/Search?keyword=%E7%8B%97%E7%B2%AE&enc=utf-8&wq=%E7%8B%97%E7%B2%AE&pvid=0b98b08c098c4269bc0838950d9c2688"
    html = urlopen(url).read().decode('utf-8')
    regex = re.compile('<li data-sku="\d*?" class="gl-item">\s+?<div class="gl-i-wrap">\s+?<div class="p-img">\s+?<a target="_blank" title="([\w\W]+?)" href="([\w\W]+?)" onclick="[\w\W]+?">\s+?<img width="\d*?" height="\d*?" class="err-product" data-img="\d*?"[\s\S]+?src="([\w\W]+?)"[\s\S]+?</a>[\s\S]+?<div data-lease="\d*?"[\w\W]+?</div>[\s\S]+?<div class="p-price">[\s\S]+?<strong class="[\w\W]+?"[\s\S]+?data-done="\d*?"[\w\W]+?<em>[\w\W]+?</em>[\w\W]+?>([\d\D]+?)</i>')
    pattern = re.findall(regex,html)
    print(pattern)
    for i in list(pattern):
        print("name:",i[0])
        print("url:",i[1].split("//")[1])
        print("img:",i[2].split("//")[1])
        print("price:",i[3])
        print("-------------------")

    
if __name__ == '__main__':
    get_prod("狗粮")