# -*- coding: utf-8 -*-
"""
@author: Alfred
"""

import scrapy
from project.basic_items import BasicItem


class SpringerItem(BasicItem):
    """
    item for springer
    """

    title = scrapy.Field()
    subtitle = scrapy.Field()
    editors = scrapy.Field()
    series_title = scrapy.Field()
    series_volume = scrapy.Field()
    copy_right = scrapy.Field()
    publisher = scrapy.Field()
    copyright_holder = scrapy.Field()
    ebook_isbn = scrapy.Field()
    doi = scrapy.Field()
    hardcover_isbn = scrapy.Field()
    softcover_isbn = scrapy.Field()
    series_issn = scrapy.Field()
    edition_number = scrapy.Field()
    page_num = scrapy.Field()
    illu_table_num = scrapy.Field()
    topics = scrapy.Field()
    editors = scrapy.Field()
    file = scrapy.Field()

    def __init__(self):
        BasicItem.__init__(self)
