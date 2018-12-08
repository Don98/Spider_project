# -*- coding: utf-8 -*-
import scrapy
from Biqu.items import BiquItem,NovelItem,ChapterItem
import os
path = 'D:\spider_project\get_novel\Biqu\biqu_novel\\'
class BiquSpider(scrapy.Spider):
    name = 'biqu'
    # allowed_domains = ['www.biqu.com']
    start_urls = ['http://www.biquge.com']
    def chapter(self,response):
        if not os.path.isdir('biqu_novel'):
            os.mkdir('biqu_novel')
        os.chdir(path)
        print(response.path('//title/text()').extract())
        print("*"*60)   
        
    def parse(self, response):
        type_list = response.xpath('//div[@class="nav"]/ul/li')
        for type in type_list:
            item = BiquItem()
            item['type_link'] = type.xpath('./a/@href').extract()[0]
            print('/'*50)
            yield scrapy.Request(item['type_link'],callback = self.chapter)
    

        