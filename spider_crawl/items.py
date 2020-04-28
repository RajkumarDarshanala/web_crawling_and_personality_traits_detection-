# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    movie = scrapy.Field()
    # price = scrapy.Field()
    image_link = scrapy.Field()
    image = scrapy.Field()
    O = scrapy.Field()
    C = scrapy.Field()
    E = scrapy.Field()
    A = scrapy.Field()
    N = scrapy.Field()
    pass
