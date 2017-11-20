import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class MySpider(CrawlSpider):
    name = 'CrawlSpiderTest'
    start_urls = ['https://baike.baidu.com/item/scrapy/7914913']

    rules = (
        Rule(LinkExtractor(allow=('/item/',)), callback='parse_item'),
    )

    def parse_item(self, response):
        item = XiaojibaItem()
        doc = pq(response.body)
        item['title'] = doc('dd.lemmaWgt-lemmaTitle-title h1').text()
        item['link'] = response.url
        item['desc'] = doc('.lemma-summary').text()
        yield item