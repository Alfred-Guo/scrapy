# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:32:57 2016

@author: Alfred
"""
from importlib import import_module

import scrapy

from project.setups import CRAWL_DICT


class myBaseSpider(scrapy.Spider):
    
    name = "base"
    
    @classmethod
    def from_crawler(cls, crawler, urls, part, suf):
        crawler.PART = part
        crawler.SUF = suf
        crawler.FILE_ = crawler.settings.get('FILE_')
        return cls(crawler, urls)

    def __init__(self, crawler, urls):
        super(myBaseSpider, self).set_crawler(crawler)
        self.urls = urls

    def start_requests(self):
        dir_name = self.settings.get('DIR_NAME')
        site = self.settings.get('SITE')

        crawl_dict = CRAWL_DICT[dir_name]

        module = import_module('.%s' % dir_name, 'project.spiders')

        callback = crawl_dict['parse']
        if type(callback) == dict:
            callback = callback[site]
        callback = getattr(module, callback)

        errback = self.baseErrback
        if 'errback' in crawl_dict.keys():
            if site in crawl_dict['errback'].keys():
                errback = crawl_dict['errback'][site]
                errback = getattr(module, errback)

        meta = {}
        if 'meta' in crawl_dict.keys():
            if site in crawl_dict['meta'].keys():
                meta = crawl_dict['meta'][site]

        for url in self.urls:
            meta['para'] = url[1].copy()
            if 'parse' in meta['para'].keys():
                parse = meta['para']['parse']
                if 'callback' in parse.keys():
                    _callback = getattr(module, parse['callback'])
                else:
                    _callback = callback
                if 'errback' in parse.keys():
                    _errback = getattr(module, parse['errback'])
                else:
                    _errback = errback
                yield scrapy.Request(url[0], callback=_callback, 
                                     errback=_errback, meta=meta.copy())
            else:
                yield scrapy.Request(url[0], callback=callback, 
                                     errback=errback, meta=meta.copy())
