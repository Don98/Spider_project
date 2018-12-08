# -*- coding:utf-8-*-
import requests
import json
import time
import random
from bs4 import BeautifulSoup
import re
from collections import Counter
import xlsxwriter

url = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=1"
keyword = input("请输入你所需要查找的关键字: ")
    
def get_jobs(url,pn = 1,kw = "python"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&gx=&isSchoolJob=1&city=%E5%B9%BF%E5%B7%9E'
    }
    data = {"first":"false","pn":pn,"kd":kw}
    r = requests.post(url,data = data,headers = headers)
    jobs_data = r.json()
    return jobs_data
    # jobs_data = jobs_data["content"]["positionResult"]["result"]
    # for i in jobs_data:
        # print(i["companyFullName"])
        # print(i["city"])
        # print(i["companyLabelList"])
        # print(i["workYear"])
        # print(i["education"])
        # print(i["salary"])
        # job_url = "https://www.lagou.com/jobs/" + str(i["positionId"]) + ".html"
        # print(job_url)

def get_max_page(jobs):
    max_page_num = jobs["content"]["pageSize"]
    return 30 if max_page_num > 30 else max_page_num
    
def read_id(jobs):
    tag = "positionId"
    page_json = jobs["content"]["positionResult"]["result"]
    company_list = []
    for i in page_json:
        company_list.append(i.get(tag))
    return company_list
    
def get_content(company_id):
    jobs_url = "https://www.lagou.com/jobs/" + str(company_id) + ".html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host': 'www.lagou.com',
        'Cookie': 'JSESSIONID=ABAAABAACBHABBIB0D40B938A14EAEE96D4254851D7B2A4; user_trace_token=20180128095608-f38ffda1-4fa5-405d-a9a6-ca3e903874cd; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517104570; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517104570; _ga=GA1.2.1594195246.1517104570; _gid=GA1.2.1758576376.1517104570; _gat=1; LGSID=20180128095610-69dda930-03ce-11e8-abb7-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGRID=20180128095610-69ddab7b-03ce-11e8-abb7-5254005c3644; LGUID=20180128095610-69ddacbd-03ce-11e8-abb7-5254005c3644; SEARCH_ID=618cfe9d82964f4f824480332d52f19e'
    }
    r = requests.get(jobs_url,headers = headers)
    return r.text
    
def get_result(content,company_id):
    soup = BeautifulSoup(content)
    job_description = soup.select('dd[class="job_bt"]')
    job_description = str(job_description[0] if len(job_description) != 0 else job_description)
    rule = re.compile(r"<[^>]+>")
    result = rule.sub("",job_description)
    return result
    
def search_skill(result):
    rule = re.compile(r'[a-zA-Z]+')
    skill_list = rule.findall(result)
    return skill_list
    
def count_skill(skill_list):
    for i in range(len(skill_list)):
        skill_list[i] = skill_list[i].lower() 
    count_dict = Counter(skill_list).most_common(80)
    return count_dict

def save_excel(count_dict,file_name):
    book = xlsxwriter.Workbook(r'D:\spider_project\jingfeng_project\{0}.xls'.format(file_name))
    tmp = book.add_worksheet()
    row_num = len(count_dict)
    for i in range(1,row_num):
        if i == 1:
            tag_pos = 'A%s' % i
            tmp.write_row(tag_pos,['关键词','频次'])
        else:
            con_pos = 'A%s' % i
            k_v = list(count_dict[i-2])
            tmp.write_row(con_pos,k_v)
    chart1 = book.add_chart({'type':'area'})
    chart1.add_series({
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$80',
        'values': '=Sheet1!$B2:$B$80'
    })
    chart1.set_title({'name':'关键词排名'})
    chart1.set_x_axis({'name':'关键词'})
    chart1.set_y_axis({'name':'频次(/次)'})
    tmp.insert_chart('C2',chart1,{'x_offset':15,'y_offset':10})
    book.close()
    
if __name__ == "__main__":
    start = time.time()
    jobs = get_jobs(url,pn = 1 ,kw = keyword)
    max_page = get_max_page(jobs)
    fin_skill_list = []
    for page in range(1,max_page + 1):
        print('--------正在抓取第%d页的信息-------' % page)
        jobs = get_jobs(url,pn = page,kw = keyword)
        time.sleep(random.randint(10,20))
        company_list = read_id(jobs)
        for company_id in company_list:
            content = get_content(company_id)
            result = get_result(content,company_id)
            skill_list = search_skill(result)
            fin_skill_list.extend(skill_list)
        print('--------开始统计关键字出现的频率-------')
    count_dict = count_skill(fin_skill_list)
    file_name = input('请输入要保存文件名：')
    save_excel(count_dict,file_name)
    print('-----正在保存-----')
    f = open("1.txt","a")
    for i in count_dict:
        f.write(str(i))
        f.write("\n")
    f.close()
    end = time.time()
    print("Spend %d seconds" % (end - start))