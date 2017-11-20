# -*- coding:utf-8 -*-
import scrapy

from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class WeiBoSpider(scrapy.Spider):
    name = 'weibo'

    start_urls = [
        'https://weibo.com/?category=0'
    ]

    def parse(self, response):
        item = XiaojibaItem()
        doc = pq(response.body)

        print doc

        for urls in doc('#PCD_pictext_i_v5 ul div[action-type="feed_list_item"]').items():
            print '------------------'
            print urls.attr('class')
            print '------------------'
            # item['title'] = urls.text()
            # item['link'] = response.url
            # item['content'] = doc('.lemma-summary').text()
            # yield item
