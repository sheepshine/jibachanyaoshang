# -*- coding:utf-8 -*-
import scrapy

from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class DmozSpider(scrapy.Spider):
    name = 'dmoz'

    start_urls = [
        'https://baike.baidu.com/item/%E6%98%8E%E6%97%A5%E8%8A%B1%E7%BB%AE%E7%BD%97'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 3
    }

    def parse(self, response):
        item = XiaojibaItem()
        doc = pq(response.body)
        item['title'] = doc('dd.lemmaWgt-lemmaTitle-title h1').text()
        item['link'] = response.url
        item['content'] = doc('.lemma-summary').text()
        yield item

        for urls in doc('.body-wrapper a[href^="/item/"]').items():
            url = 'https://baike.baidu.com' + urls.attr('href')
            yield scrapy.Request(url, callback=self.parse)
