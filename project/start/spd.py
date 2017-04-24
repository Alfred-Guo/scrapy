# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
import os
from math import ceil
from datetime import datetime as dt

import sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from spiders.base import BaseSpider


class Spd():
    """
    basic class used for multiple spiders
    """

    def __init__(self, custom_settings):
        #os.environ['SCRAPY_SETTINGS_MODULE'] = 'project.settings'

        self.custom_settings = {
            'DATE': dt.today().strftime('%Y-%m-%d'),
            'DATA_PATH': PATH + '/data',
        }
        self.custom_settings.update(custom_settings)
        self.custom_settings['FILE_PATH'] = self._file_path()

    def get_urls(self):
        """
        generate the urls to crawl. Should be overrided in a child class
        """
        raise NotImplementedError

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

        if self.custom_settings.get('PARTITION', True):
            urls = self._partition(urls, num)
        for url in urls:
            process.crawl(spider, urls=url)
        process.start()

    @staticmethod
    def _partition(data_list, num):
        """
        cut url list
        """
        delta = ceil(len(data_list) / num)
        partition = range(0, len(data_list), delta)
        return [data_list[i:i + delta] for i in partition]

    def _file_path(self):
        file_path = '{data_path}/{dir_name}/{site}_{date}.csv'.format(
            data_path=self.custom_settings.get('DATA_PATH', ''),
            dir_name=self.custom_settings.get('DIR_NAME', ''),
            site=self.custom_settings.get('SITE', ''),
            date=self.custom_settings['DATE'],
        )
        file_path = self.custom_settings.get('FILE_PATH', file_path)

        if self.custom_settings.get('MODE', 'w') == 'w':
            if os.path.isfile(file_path):
                os.remove(file_path)
        if not os.path.isdir(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        return file_path
