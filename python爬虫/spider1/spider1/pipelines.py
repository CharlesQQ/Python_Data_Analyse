# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib
class Spider1Pipeline(object):
    def process_item(self, item, spider):

        ab_src = "http://www.xiaohuar.com" + item['src']
        file_name = item['name'].encode("utf-8")+".jpg"
        # file_name = str(i)+".jpg"
        file_path = os.path.join(u'C:\\图片\\',file_name)
        urllib.urlretrieve(ab_src,file_path)
        # if src:
        #     ab_src = "http://www.xiaohuar.com" + src[0]
        #     file_name = "%s_%s.jpg" % (school[0].encode('utf-8'), name[0].encode('utf-8'))
        #     file_path = os.path.join("/Users/wupeiqi/PycharmProjects/beauty/pic", file_name)
        #     urllib.urlretrieve(ab_src, file_path)

        return item
