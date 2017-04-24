# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:32:57 2016

@author: Alfred
"""
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
        for name, func in self.settings['PARSE'].items():
            setattr(self, name, func)
        for url, meta in self.urls:
            yield scrapy.Request(
                url=url,
                callback=getattr(self, self.settings.get('CALLBACK')),
                errback=self.settings.get('ERRORBACK', self.errback),
                meta={'para': meta.copy()}
            )

    def parse(self, response):
        pass

    @staticmethod
    def errback():
        pass
