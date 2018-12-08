# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItcastPipeline(object):
    def __init__(self):
        self.f = open("itcast_pipeline.json","w")
    def process_item(self, item, spider):
        content = (json.dumps(dict(item),ensure_ascii = False) + ", \n").encode('utf-8')
        self.f.write(str(content))
        return item
    def close_spider(self,spider):
        self.f.close()
