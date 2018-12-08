# -*- coding: utf-8 -*-

import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'Itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath("./h3/text()").extract()[0]
            item['title'] = node.xpath("./h4/text()").extract()[0]
            item['info'] = node.xpath("./p/text()").extract()[0]
            yield item