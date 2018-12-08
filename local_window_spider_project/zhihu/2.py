#coding : utf-8
import requests
import re
headers = {
"cookie": '''你们自己填坑''',
"referer": "https://www.zhihu.com/",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

#得到内容
def get_content(url):
    response = requests.get(url,headers = headers)
    return str(response.content.decode('utf-8'))
#处理数据
def get_something(a):
    price = re.findall(re.compile('"original_price":([\w\W]+?),'),a)
    tag = re.findall(re.compile('"tags":[[\w\W]+?]'),a)
    style = re.findall(re.compile('"name": "([\w\W]+?)"'),str(tag))
    title = re.findall(re.compile('"subject": "([\w\W]+?)"'),a)
    speaker = re.findall(re.compile('"speaker":[\w\W]+?"member"[\w\W]+?, "role"'),a)
    name = re.findall(re.compile('], "name": "([\w\W]+?)", "url": "'),str(speaker))
    return price , style , title ,name
    
if __name__ == '__main__':
    main_url = "https://api.zhihu.com/lives/homefeed?includes=live"
    a = get_content(main_url)
    price , style , title ,name= get_something(a)
    for i in range(len(price)):
        print("题目是：" , title[i])
        print("作者是：" , name[i])
        print("价格是：",int(price[i]) / 100)
        print("类型是：", style[i])
        print("="*100)