# -*- coding:utf-8 -*-
import scrapy

from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class DmozSpider(scrapy.Spider):
    name = 'dmoz'

    start_urls = [
        'https://baike.baidu.com/item/%E6%98%8E%E6%97%A5%E8%8A%B1%E7%BB%AE%E7%BD%97'
    ]

    def parse(self, response):
        item = XiaojibaItem()
        item['title'] = pq(response.body).find('dd.lemmaWgt-lemmaTitle-title h1').text()
        item['link'] = response.url
        item['desc'] = pq(response.body).find('.lemma-summary').text()
        yield item
        