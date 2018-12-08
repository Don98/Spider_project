import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

if __name__ == '__main__':
    # url = "http://www.seav9.com/forum.php?mod=viewthread&tid=7188014&extra=page%3D1%26filter%3Dtypeid%26typeid%3D3"
    url = 'http://www.seav9.com/forum.php?mod=forumdisplay&fid=46'
    response = requests.get(url,headers = headers)
    content = response.content.decode('utf-8','ignore')
    with open('2.html','w',encoding = 'utf-8') as f:
        f.write(str(content))