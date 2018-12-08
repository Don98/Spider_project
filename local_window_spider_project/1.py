import requests
import re

headers = {"User-Agen":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

if __name__ == '__main__':
    response = requests.get('https://www.63ng.com',headers = headers)
    print(respo.content.decode('utf-8'))