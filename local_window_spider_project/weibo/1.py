# coding : utf-8
import requests
import re
import csv
import os 
import time
from ip import ip
from us import us
import random
from multiprocessing import Pool
# http://s.weibo.com/ajax/comment/small?act=list&mid=4253639951843300&uid=5252283558&smartFlag=false&smartCardComment=&isMain=true&suda-data=key%253Dtblog_search_weibo%2526value%253Dweibo_ss_18_p_p&pageid=weibo&_t=0&__rnd=1529985647899
LZurl = "https://m.weibo.cn/statuses/extend?id="
the_one = ["https://m.weibo.cn/api/container/getIndex?type=all&queryVal=@南方航空&luicode=10000011&lfid=100103type%3D1%26q%3D@南方航空&title=@南方航空&containerid=100103type%3D1%26q%3D@南方航空&page=","https://m.weibo.cn/api/container/getIndex?type=all&queryVal=@南航&luicode=10000011&lfid=100103type%3D1%26q%3D@南航&title=@南航&containerid=100103type%3D1%26q%3D@南航&page=","https://m.weibo.cn/api/container/getIndex?type=all&queryVal=@南航客户服务中心&luicode=10000011&lfid=100103type%3D1%26q%3D@南航客户服务中心&title=@南航客户服务中心&containerid=100103type%3D1%26q%3D@南航客户服务中心&page="]
the_two = ["https://m.weibo.cn/api/container/getIndex?type=all&queryVal=@中国国际航空&luicode=10000011&lfid=100103type%3D1%26q%3D@中国国际航空&title=@中国国际航空&containerid=100103type%3D1%26q%3D@中国国际航空&page=","https://m.weibo.cn/api/container/getIndex?type=all&queryVal=@国航&luicode=10000011&lfid=100103type%3D1%26q%3D@国航&title=@国航&containerid=100103type%3D1%26q%3D@国航&page=","https://m.weibo.cn/api/container/getIndex?type=all&queryVal=@国航小秘书&luicode=10000011&lfid=100103type%3D1%26q%3D@国航小秘书&title=@国航小秘书&containerid=100103type%3D1%26q%3D@国航小秘书&page="]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

def remove_emoji(s):
    s = re.compile(u"\u200b").sub('', s)
    s = re.compile(u"\u200c").sub('', s)
    s = re.compile(u"\u200d").sub('', s)
    s = re.compile(u"\ud83d").sub('', s)
    s = re.compile(u"\ude0a").sub('', s)
    s = re.compile(u"\ud83c").sub('', s)
    # s = re.compile(u"\ude0a").sub('', s)
    return s
def get_LZ_content(url,id):
    url += str(id)
    response = requests.get(url,headers = {"User-Agent":us[random.randint(0,len(us)-1)]},proxies = ip[random.randint(0,len(ip)-1)])
    html = str(response.content.decode('unicode_escape'))
    html = re.sub(re.compile('<[\w\W]+?>'),"",html)
    html = remove_emoji(html)
    longTextContent = re.findall(re.compile('"longTextContent":"([\w\W]+?)"'),html)
    # print(longTextContent)
    comments_count = re.findall(re.compile('"comments_count":([\w\W]+?),'),html)
    # print(comments_count[0])
    PLurl = "https://m.weibo.cn/api/comments/show?id=" + str(id) + "&page="
    return longTextContent[0],comments_count[0],PLurl
    
def get_content(url,i):
    a = us[random.randint(0,len(us)-1)]
    b = ip[random.randint(0,len(ip)-1)]
    url += str(i)
    # print(url)
    response = requests.get(url,headers = {"User-Agent":us[random.randint(0,len(us)-1)]},proxies = ip[random.randint(0,len(ip)-1)],timeout = 10)
    html = str(response.content.decode('unicode_escape'))
    html = remove_emoji(html)
    create_times = re.findall(re.compile('"created_at":"([\w\W]+?)"'),html)
    # print(create_time)
    user_names = re.findall(re.compile('"screen_name":"([\w\W]+?)",'),html)
    # print(user_names)
    html = re.sub(re.compile('<[\w\W]+?>'),"",html)
    texts = re.findall(re.compile('"text":"([\w\W]+?)"'),html)
    # print(texts)
    return create_times,user_names,texts
    
def get_all_content(url,j):
    url += str(j)
    response = requests.get(url,headers = {"User-Agent":us[random.randint(0,len(us)-1)]},proxies = ip[random.randint(0,len(ip)-1)])
    html = str(response.content.decode('unicode_escape'))
    html = str(response.content.decode('utf-8').encode('gbk','ignore'))
    html = remove_emoji(html)
    # print(html)
    ids = re.findall(re.compile('"mid":"([\w\W]+?)"'),html)
    return ids
    # with open('2.txt','w',encoding = 'utf-8') as f:
        # f.write(str(html.encode('utf-8',"ignore")))
    
def to_filter(user_names,name):
    for i in user_names:
        if name[0] == i or name[1] == i or name[2] == i:
            return 1
    return 0
        
def get_specify(b):
    flag = 0
    for i in range(len(b)):
        if b[i] == "\\":
            start = i
            flag = 1
        if flag and b[i] == "'":
            end = i
            flag = 0
    return start , end 
    
def to_try(a,L,counter):
    counter += 1
    if counter >= 10:
        return
    try:
        a.writerow(L)
    except UnicodeEncodeError as b:
        start , end = get_specify(str(b))
        c = str(b)[start:end]
        for k in range(len(L)):
            L[k] = re.compile(c).sub('', L[k])
        to_try(a,L,counter)  

all_id = []
   
def work(name,all_urls):
    num = 0
    with open(name[0] + '.csv','w',newline = "") as csvfile:
        a = csv.writer(csvfile,dialect='excel')
        L = ['LZ','time','user_name','response']            
        a.writerow(L)
    for all_url in all_urls:
        for j in range(1,1500):
            print(str((j / 15)) + "%" + "    目前已收集了" + str(num) + "条")
            ids = get_all_content(all_url,j)
            for id in ids:
                if id in all_id:
                    continue
                else:
                    all_id.append(id)
                # print(id)
                p = Pool()
                try:
                    longTextContent,comments_count ,PLurl = get_LZ_content(LZurl,id)
                except:
                    continue
                create_times,user_names,texts = p.apply_async(get_content,args = (PLurl,1)).get()
                # create_times,user_names,texts = get_content(PLurl,1)
                # print(p.apply_async(get_content,args = (PLurl,1)).get())
                # exit()
                for i in range(2,int(comments_count) // 18):
                    a , b ,c = p.apply_async(get_content,args = (PLurl,i)).get()
                    # a , b ,c = get_content(PLurl,i)
                    create_times += a
                    user_names += b
                    texts += c
                p.close()
                p.join()
                # ids = get_all_content(all_url)
                # print(create_times)
                flag = to_filter(user_names,name)
                num += flag
                # print("目前已收集了" + str(num) + "条")
                if not flag:
                    continue
                if len(create_times) == 0:
                    continue

                with open(name[0] + '.csv','a',newline = "") as csvfile:
                    a = csv.writer(csvfile,dialect='excel')
                    L = [0] * 4
                    L[0] = longTextContent
                    L[1] = create_times[0]
                    L[2] = user_names[0]
                    L[3] = texts[0]
                    counter = 0
                    to_try(a,L,counter)
                    for i in range(1,len(texts)):
                        L = [" "]
                        L.append(create_times[i])
                        L.append(user_names[i])
                        L.append(texts[i])
                        # print(L)
                        counter = 0
                        to_try(a,L,counter)
                # time.sleep(5)
        # with open('1.txt','w',encoding = 'utf-8') as f:
            # f.write(str(response.content.decode('unicode_escape')))
   
if __name__ == '__main__':
    name = ['南方航空','南航','南航客户服务中心']
    # work(name,the_one)
    name = ['中国国际航空','国航小秘书','国航']
    work(name,the_two)