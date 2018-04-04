# -*- coding:utf-8 -*-
import requests
import smtplib
import getpass
from bs4 import BeautifulSoup
import re
from email.mime.text import MIMEText
from email.header import Header

def get_weather(city):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    url = "http://m.sohu.com/weather/?city=" + city
    r = requests.get(url,headers = headers)
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    city = soup.find("a",class_="site").text
    print(city)
    current = soup.find("p",{"class":"cur"}).text
    print("现在温度：" + current)
    low = soup.find("em",{"class":"lowest"}).text
    high = soup.find("em",{"class":"highest"}).text
    print("最低温度：%s\n最高温度：%s"%(low,high))
    stat = soup.find("em",class_="stat").text
    print(stat)
    pm = soup.find("div",class_="pm")
    pm_25 , air_quality = map(lambda x: x.text,pm)
    print("pm2.5：%s\n空气质量：%s" % (pm_25,air_quality))
    return city + "\n现在温度：" + current + "\n最低温度：" + low + "\n最高温度：" + high + "\npm2.5：" + pm_25 + "\n空气质量：" + air_quality
    
def send_email(result):
    sender = input('From: ')
    password = getpass.getpass('Password: ')
    smtp_server = input('SMTP server: ')#'smtp.163.com'
    receivers = ['ZHONGDAchenqd6@163.com']
    
    message = MIMEText(result,'plain','utf-8')
    message['From'] = Header(sender,'utf-8')
    message['to'] = Header(receivers[0],'utf-8')
    message['Subject'] = Header('您的天气预报','utf-8')
    
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(sender,password)
    server.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功!')
    server.quit()
    
if __name__ == '__main__':
    city = input("(如果输入错误则自动输出当前城市天气)\n请输入你要查询的城市：")
    result = get_weather(city)
    send_email(result)