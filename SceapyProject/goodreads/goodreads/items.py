# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # idtag= scrapy.Field()
    url=scrapy.Field()
    gl=scrapy.Field()
