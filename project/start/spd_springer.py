# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
from spd import Spd


class Springer(Spd):
    """
    springer spider
    """

    def __init__(self):
        custome_settings={
            'DIR_NAME': 'springer',
            'SITE': 'springer',
        }
        super(Springer, self).__init__(custome_settings)

    @staticmethod
    def get_urls():
        """
        generate the book url to crawl
        """

        return [('http://www.springer.com/cn/book/9781461471370',
                 {'file': 'test'})]


if __name__ == '__main__':
    springer = Springer()
    springer.start_crawl()
