#coding : utf-8
import requests
import re
headers = {
"cookie": '''_zap=7c7470ca-1e7c-440a-9796-eecf4d38b516; z_c0="2|1:0|10:1519821703|4:z_c0|92:Mi4xUno2ckJRQUFBQUFBWUMwbExDODNEU1lBQUFCZ0FsVk5oX0dEV3dCLUxRY2JxdUIweXZpRWRnd01uVDFtamxuZURR|8829787b161c0ac8a359826e1167e22ba942988237e92792758a83831717b6cd"; __DAYU_PP=BiiaBj7Zen2UNfmRzbyq20d231854a42; d_c0="AJAgybI8iA2PTiF1-pqTqkmiu70lSkjAvFM=|1525261016"; q_c1=7928b2b4c1c04b6a89d80f727fc50b9b|1525261275000|1512121450000; _xsrf=11192827-0088-46bd-a90e-da33b3c30283; __utma=155987696.909849749.1526645543.1526645543.1526645543.1; __utmb=155987696.0.10.1526645543; __utmc=155987696; __utmz=155987696.1526645543.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)''',
"referer": "https://www.zhihu.com/",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
# <div class="LiveFeedsPage-page-1ExD Card-group-1iQj Card-card-102t Card-notSafari-3UQA" id="feedLives"></div>
def get_content(url):
    response = requests.get(url,headers = headers)
    return str(response.content.decode('utf-8'))

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