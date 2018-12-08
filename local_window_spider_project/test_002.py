import urllib.request

url = "http://www.baidu.com"

user_agent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"

headers = {'User-Agent':user_agent}

req = urllib.request.Request(url,headers = headers)

response = urllib.request.urlopen(req)

the_page = response.read()

print(the_page)
# https://tieba.baidu.com/f?kw=%E4%BC%AA%E5%A8%98&ie=utf-8&pn=0
# https://tieba.baidu.com/f?kw=%E4%BC%AA%E5%A8%98&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=%E4%BC%AA%E5%A8%98&ie=utf-8&pn=100