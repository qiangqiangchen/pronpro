# -*- coding:utf-8 -*-
import scrapy
import sys
import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pornpro.items import PornproItem
class pornproSpider(CrawlSpider):
    name='pornpro'
    allowed_domains=["91.p9a.space"]
    base_url='http://91.p9a.space/'
    page_base_url='http://91.p9a.space/forumdisplay.php?fid=19&page='
    page_base_url1='http://91.p9a.space/forumdisplay.php?fid=21&page='
    start_urls=[page_base_url1+str(i) for i in range(1,421)]
    
    def parse(self,response):
        items=PornproItem()
        pro_list=response.xpath('//tbody[starts-with(@id,"normalthread_")]')
        for pro_item in pro_list:
            items['title']=pro_item.xpath('./tr/th/span/a/text()').extract()[0]
            items['title_url']=pro_item.xpath('./tr/th/span/a/@href').extract()[0]
            items['author']=pro_item.xpath('./tr/td[@class="author"]/cite/a/text()').extract()[0]
            items['creat_time']=pro_item.xpath('./tr/td[@class="author"]/em/text()').extract()[0]
            items['replycount']=pro_item.xpath('./tr/td[@class="nums"]/strong/text()').extract()[0]
            items['viewcount']=pro_item.xpath('./tr/td[@class="nums"]/em/text()').extract()[0]
            yield items
