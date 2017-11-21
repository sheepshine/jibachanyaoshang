# -*- coding:utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.exceptions import CloseSpider

from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class taptapDailySpider(scrapy.Spider):
    name = 'taptapDaily'

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }

    start_urls = [
        'https://www.taptap.com/category/e381'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 3
    }

    curIndex = 1

    def start_requests(self):
            yield Request(self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        item = XiaojibaItem()
        doc = pq(response.body)

        print '--------------'
        print len(doc('.taptap-app-list .taptap-app-item'))
        print '--------------'

        if (len(doc('.taptap-app-list .taptap-app-item')) == 0):
            print "无更多数据，close spider"
            raise CloseSpider(reason="no more data")

        for urls in doc('.taptap-app-list .taptap-app-item').items():
            item['title'] = urls.find('.item-caption-title.flex-text-overflow .flex-text').text()
            item['link'] = urls.find('.item-caption-title.flex-text-overflow').attr('href')
            item['content'] = urls.find('.item-caption-label a').text()
            yield item

        self.curIndex += 1
        print self.curIndex
        url = 'https://www.taptap.com/category/e381?page=%s' % self.curIndex
        print url
        yield Request(url, headers=self.headers, callback=self.parse)