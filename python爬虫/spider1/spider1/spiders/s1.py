#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'

import scrapy

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "nnnnn"       #必须要写，相当于app的名字，需要执行的app，可以写多个

    # allowed_domains = ["xiaohuar.com"]

    start_urls = [                          #定义起始url
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):                 #回调函数，自动执行
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
        print body