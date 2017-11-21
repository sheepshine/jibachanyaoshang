# -*- coding:utf-8 -*-
import scrapy

from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class WeiBoSpider(scrapy.Spider):
    name = 'weibo'

    start_urls = [
        'https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page=0&lefnav=0&__rnd=1511229965587'
    ]

    def parse(self, response):
        item = XiaojibaItem()
        doc = pq(response.body)

        for urls in doc('div[action-type="feed_list_item"]').items():
            print '------------------'
            print urls.attr('class')
            print '------------------'
            item['title'] = urls.text()
            item['link'] = response.url
            item['content'] = doc('.lemma-summary').text()
            yield item
