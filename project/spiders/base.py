# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:32:57 2016

@author: Alfred
"""
from importlib import import_module

import scrapy


class BaseSpider(scrapy.Spider):
    """
    base spider used for all crawling
    """

    name = "base"

    def __init__(self, urls):
        super(BaseSpider, self).__init__()
        self.urls = urls

    def start_requests(self):
        """
        start crawl
        """
        
        crawl_dict = self.settings.get('CRAWL_DICT')
        dir_name = self.settings.get('DIR_NAME')
        site = self.settings.get('SITE')

        para = {}
        module = import_module('.%s' % dir_name, 'project.spiders')

        callback = crawl_dict['parse']
        if isinstance(callback, dict):
            callback = callback[site]
        para['callback'] = getattr(module, callback)

        errback = crawl_dict.get('errback', {}).get(site)
        if errback:
            para['errback'] = getattr(module, errback)

        for url in self.urls:
            para['url'] = url[0]
            para['meta'] = {'para': url[1].copy()}
            yield scrapy.Request(**para)

    def parse(self, response):
        pass
