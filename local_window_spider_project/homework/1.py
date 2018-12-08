import requests

headers = {"Referer":"http://nlp.sysu.edu.cn/c/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
"X-GWT-Module-Base":"http://nlp.sysu.edu.cn/c/cong/",
"X-GWT-Permutation":"38F73CF6B7433E0AEC4F39EB14FA3332"}
a = {2:"17343010@mail2.sysu.edu.cn",6:"cqd19980929"}
payload = a

if __name__ == '__main__':
    url = "http://nlp.sysu.edu.cn/c/#"
    # url = "http://nlp.sysu.edu.cn/c/cong/course"
    response = requests.post(url , headers = headers)
    req = response.content.decode('utf-8')
    with open('2.html','w',encoding = 'utf-8') as f:
        f.write(str(req))