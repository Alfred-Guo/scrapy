# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from project.basicItems import basicItem


class springerItem(basicItem):
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
    
    def __init__(self):
        basicItem.__init__(self)
