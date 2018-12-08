import requests
import re
import os

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", str(title))  # 替换为下划线
    return new_title

def download_articles(url):
    response = requests.get(url)
    title = re.compile('<title>([\w\W]+?)</title>').findall(response.text)
    title = validateTitle(title[0] if len(title) !=0 else title)
    content = re.compile('<p[\w\W]+?>([\w\W]+?)</p>').findall(response.text) 
    f = open('%s.txt' % title,'w')
    f.write(str(title.encode('utf-8')))
    t = 0
    for i in content:
        t += 1
        if t >= len(content)-21 or t <= 5:
            continue
        if 'data-src=' in i:
            f.write(re.compile('data-src="([\w\W]+?)"').findall(i)[0])
            f.write('\n')
            continue
        if i.startswith('<'):
            j = re.compile('<strong>([\w\W]+?)</strong>').findall(i)
            f.write(j[0] if len(j) !=0 else ' ')
        else:
            try:
                f.write(i.replace("<br  />","\n").replace("&nbsp;","\n"))
            except UnicodeEncodeError:
                continue
            finally:
                f.write('\n')
    f.close()

def deal_title(title_list):
    for i in range(len(title_list)):
        title_list[i] = title_list[i].replace(' ','_')
    return title_list
    
def list_count(L,a,start,end):
    t = 0
    for i in range(start,end+1):
        if L[i] == a:
            t += 1
    return t

def get_something():
    url = 'http://mp.weixin.qq.com/s/-j4u6Q4KpAfTQZnlaO0vgw'
    response = requests.get(url,'utf-8')
    url_list = re.compile('<a href="([\w\W]+?)" target="_blank"').findall(response.text)
    title_list = re.compile('>(\d+\.[\w\W]+?)<').findall(response.text)
    return response,url_list,title_list
    
def deal_url(url_list):
    for i in range(len(url_list)):
        for j in range(i+1,len(url_list)):
            if url_list[i] == url_list[j]:
                url_list[j] = " "
    return url_list
    
if __name__ == '__main__':
    response,url_list,title_list = get_something()
    url_list = deal_url(url_list)
    del title_list[5]
    articles_nums = [25,8,5,87,99,53,7,5,5,50,68,12,12,37]
    count = 0
    title_list = deal_title(title_list)
    t = 0
    os.chdir('python')
    path = os.getcwd()
    if not os.path.isdir(title_list[0]):
        os.system('mkdir ' + title_list[0])
        os.chdir(title_list[0])
    for url in url_list:
        if url == " ":
            continue
        download_articles(url)
        count += 1
        if t != 14 and count >= articles_nums[t]:
            t += 1
            count = 0
            os.chdir(path)
            if not os.path.isdir(title_list[t]):
                os.system('mkdir ' + title_list[t])
            os.chdir(title_list[t])
            print(title_list[t])
        print(count)