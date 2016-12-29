# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
from spd import Spd

class Springer(Spd):
    def __init__(self):
        super(Springer,self).__init__('springer','springer')
    
    def getUrls(self):
        return [('http://www.springer.com/cn/book/9781461471370',{'file':'te'})]
                
if __name__=='__main__':
    springer=Springer()
    springer.start_crawl()
