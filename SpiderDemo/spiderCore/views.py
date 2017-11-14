# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from .utils import response
from .spiderInsider import spider_main


def index(request):
    return HttpResponse('hello world!')


def add_article(request, new_article):
    try:
        models.Article.objects.create(new_article)
        return response.response_fn_success("success")
    except Exception as e:
        return response.response_fn_error(e)


def start_request(request):
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = spider_main.SpiderMan()
    obj_spider.craw(root_url, 100)
    return response.response_fn_success("success")

