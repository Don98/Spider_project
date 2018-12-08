# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UseScrapySipderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#teacher
class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()