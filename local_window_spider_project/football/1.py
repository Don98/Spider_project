import requests
import re

url = "http://odds.500.com/fenxi/bifen-705830.shtml"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","Referer":"http://odds.500.com/fenxi/bifen-705830.shtml"}


if __name__ == '__main__':
    response = requests.get(url,headers = headers)
    req = response.content.decode("utf-8",'ignore')
    