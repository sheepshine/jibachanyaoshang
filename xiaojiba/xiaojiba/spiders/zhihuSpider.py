# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

from xiaojiba.items import XiaojibaItem
from pyquery import PyQuery as pq


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.zhihu.com/"
    }

    start_urls = [
        'https://www.zhihu.com/'
    ]

    def start_requests(self):
        return [Request("http://www.zhihu.com/#signin",
                        meta={'cookiejar': 1},
                        callback=self.post_login)]  # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数

    def post_login(self, response):
        print 'Preparing login'
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = pq('input[name="_xsrf"]').val()
        print xsrf

        return [FormRequest(
            url='https://www.zhihu.com/login/phone_num',
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata={
                '_xsrf': xsrf,
                'email': '123456',
                'password': '123456'
            },
            callback=self.after_login,
            dont_filter=True
        )]

    def after_login(self, response):
        print '------------------'
        print response
        print '------------------'
        yield Request(
            'http://www.zhihu.com',
            headers=self.headers,
            callback=self.page_content,
            dont_filter=True,
        )

    def page_content(self, response):
        print response.body