# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PornproItem(scrapy.Item):
    title=scrapy.Field()
    title_url=scrapy.Field()
    author=scrapy.Field()
    creat_time=scrapy.Field()
    replycount=scrapy.Field()
    viewcount=scrapy.Field()
