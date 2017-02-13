# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:56:24 2016

@author: Alfred
"""
CRAWL_DICT = {
    'springer': {
        'domains': ['springer.com'],
        'parse': 'springer',
        'field_to_export': [
            'title', 'subtitle', 'editors', 'series_title', 
            'series_volume', 'copy_right', 'publisher', 
            'copyright_holder', 'ebook_isbn', 'doi', 'hardcover_isbn', 
            'softcover_isbn', 'series_issn', 'edition_number', 
            'page_num', 'illu_table_num', 'topics', 'editors', 'url', 
            'create_date'
        ],
        # 'meta': {'foo': {}},
        # 'errback': {'foo': ''},
    },
}
