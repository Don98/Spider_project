# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiquItem(scrapy.Item):
    # define the fields for your item here like:
    type_link = scrapy.Field()

class NovelItem(scrapy.Item):
    novel_names = scrapy.Field()
    novle_links = scrapy.Field()
    
class ChapterItem(scrapy.Item):
    title_names = scrapy.Field()
    content = scrapy.Field()