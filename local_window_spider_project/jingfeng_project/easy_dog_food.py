# -*- coding:utf-8 -*-

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

def get_prod(keyword):
    # url = "https://search.jd.com/Search?keyword = " + quote(keyword) + "&enc=utf-8"
    url = "https://search.jd.com/Search?keyword=%E7%8B%97%E7%B2%AE&enc=utf-8&wq=%E7%8B%97%E7%B2%AE&pvid=0b98b08c098c4269bc0838950d9c2688"
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html)
    li_all = soup.find_all('li',"gl-item")
    for i in li_all:
        print(i.a["title"])
        print(i.a["href"])
        img = i.img["src"] if "src" in i.img else i.img.get("data-lazy-img")
        print("img:",img)
        print(i.i)
        
if __name__ == "__main__":
    get_prod("狗粮")