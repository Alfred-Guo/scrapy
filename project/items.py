# -*- coding: utf-8 -*-
"""
@author: Alfred
"""
import scrapy


class Item(scrapy.Item):
    def __init__(self, dir_name):
        super(Item, self).__init__()
        for i in CRAWL_DICT[dir_name]['field_to_export']:
            self.fields[i] = {}
