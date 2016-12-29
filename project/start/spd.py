# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
class Spd():
    def __init__(self,dir_name,site,custom_settings={}):
        os.environ['SCRAPY_SETTINGS_MODULE']='project.settings'
        self.suf=''
        self.dir_name=dir_name
        self.site=site
        self.custom_settings={
            'DIR_NAME':dir_name,
            'SITE':site,
        }
        for i in custom_settings.keys():
            self.custom_settings=custom_settings[i]
        self.clean()
        
    def clean(self):
        pass
    
    def getUrls(self):
        pass
    
    def start_crawl(self,num=1):
        urls=self.getUrls()
        if urls:
            self._crawl(self.custom_settings,urls,num)
            
    def _crawl(self,custom_settings,urls,num=5):
        from scrapy.utils.project import get_project_settings
        from scrapy.crawler import CrawlerProcess
        
        project_settings=get_project_settings()
        print(project_settings.getdict('ITEM_PIPELINES'))
        for key in custom_settings:
            project_settings[key]=custom_settings[key]
        process=CrawlerProcess(project_settings)
        
        from project.spiders.base import myBaseSpider
        spider=myBaseSpider
        
        urls=self._partition(urls,num)
        for i in range(len(urls)):
            process.crawl(spider,urls=urls[i],part=i,suf=self.suf)
            process.start()
                    
    def _partition(self,_list,num):
        from math import ceil
        delta=ceil(len(_list)/num)
        partition=range(0,len(_list),delta)
        return [_list[i:i+delta] for i in partition]
