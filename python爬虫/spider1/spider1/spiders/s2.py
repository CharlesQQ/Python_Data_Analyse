#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
import scrapy
import os
import urllib
class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "s2"       #必须要写，相当于app的名字，需要执行的app，可以写多个

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
        from scrapy.selector import HtmlXPathSelector
        hxs = HtmlXPathSelector(response)
        #items = hxs.select('//div[@class="item_list infinite_scroll"]/div//img/@src').extract()    #找到所有的div下clas=item_list infinite_scroll下的字div
        #items = hxs.select('//div[@class="item_list infinite_scroll"]/div[1]')   #可以通过索引查找

        from scrapy.selector import Selector
        items = Selector(response=response).xpath('//div[@class="item_list infinite_scroll"]/div')

        #items = hxs.select('//div[@class="item_list infinite_scroll"]/div')    #表示一个对象，不是具体的值
        for i in range(len(items)):
            srcs = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
            names = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
            schools = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()    #extract表示去找值
            if srcs and names and schools:
                try:
                    print names[0],schools[0],srcs[0]
                    from spider1 import items
                    obj = items.Spider1Item()
                    obj['name']=names[0]
                    obj['school']=schools[0]
                    obj['src']=srcs[0]
                    yield obj
                    """
                    ab_src = "http://www.xiaohuar.com" + srcs[0]
                    #file_name = names[0].encode("utf-8")+".jpg"
                    file_name = str(i)+".jpg"
                    file_path = os.path.join(u'C:\\图片\\',file_name)
                    urllib.urlretrieve(ab_src,file_path)
                    # if src:
                    #     ab_src = "http://www.xiaohuar.com" + src[0]
                    #     file_name = "%s_%s.jpg" % (school[0].encode('utf-8'), name[0].encode('utf-8'))
                    #     file_path = os.path.join("/Users/wupeiqi/PycharmProjects/beauty/pic", file_name)
                    #     urllib.urlretrieve(ab_src, file_path)
                """
                except Exception as e:
                    print e