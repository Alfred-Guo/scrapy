# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:41:14 2016
@author: Alfred
"""
import scrapy

class baiscItem(scrapy.Item):
    create_date=scrapy.Field()
    update_date=scrapy.Field()
    url=scrapy.Field()
    
class foo(scrapy.Item):
    pass
