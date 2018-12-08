from urllib import request

if __name__ == "__main__":
    #访问网址
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=80035161_2_dg&wd=python%E7%88%AC%E8%99%AB%E7%9A%84urllib.request%E6%80%8E%E4%B9%88%E6%9B%B4%E6%8D%A2ip%3F&oq=python%25E7%2588%25AC%25E8%2599%25AB%25E6%258A%2593%25E5%258F%2596%25E6%2580%258E%25E4%25B9%2588%25E6%2594%25B9%25E6%258D%25A2ip%25E8%25BF%259B%25E8%25A1%258C%25E8%25AF%25B7%25E6%25B1%2582%253F&rsv_pq=b16b427a00004afd&rsv_t=8acdX0ZO730yf9MWLA19gcDYyhvFwUU9ukIS9BvGHd2OYuBNlUkEPbT%2FcXEVVrT2GV%2Fe8w&rqlang=cn&rsv_enter=1&inputT=4412&rsv_sug3=84&rsv_sug1=31&rsv_sug7=100&bs=python%E7%88%AC%E8%99%AB%E6%8A%93%E5%8F%96%E6%80%8E%E4%B9%88%E6%94%B9%E6%8D%A2ip%E8%BF%9B%E8%A1%8C%E8%AF%B7%E6%B1%82%3F'
    #这是代理IP
    proxy = {'http':'106.46.136.112:808'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    f = open("2.txt","w")
    f.write(str(html.encode('utf-8')))
    f.close()
    print(html)