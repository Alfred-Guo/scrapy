# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
import os
from math import ceil
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from project.constants import CRAWL_DICT
from project.spiders.base import BaseSpider


class Spd():
    """
    basic class used for multiple spiders
    """

    def __init__(self, custom_settings):
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'project.settings'

        dir_name = custom_settings['DIR_NAME']
        self.custom_settings = {
            'CRAWL_DICT': CRAWL_DICT[dir_name],
        }
        self.custom_settings.update(custom_settings)

    def get_urls(self):
        """
        generate the urls to crawl. Should be overrided in a child class
        """
        pass

    def start_crawl(self, num=1):
        """
        start crawl
        """

        urls = self.get_urls()
        if urls:
            self._crawl(urls, num)

    def _crawl(self, urls, num):
        """
        run spider in script
        """

        project_settings = get_project_settings()
        project_settings.update(self.custom_settings)
        process = CrawlerProcess(project_settings)

        spider = BaseSpider

        urls = self._partition(urls, num)
        for i in urls:
            process.crawl(spider, urls=i)
        process.start()

    @staticmethod
    def _partition(data_list, num):
        """
        cut url list
        """

        delta = ceil(len(data_list) / num)
        partition = range(0, len(data_list), delta)
        return [data_list[i:i + delta] for i in partition]
