# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:54:36 2016

@author: Alfred
"""
from datetime import datetime as dt

from project.items import springerItem


KEYS = {
    'Book Title': 'title',
    'BookSubtitle': 'subtitle',
    'Editors': 'editors',
    'SeriesTitle': 'series_title',
    'SeriesVolume': 'series_volume',
    'Copyright': 'copy_right',
    'Publisher': 'publisher',
    'Copyright Holder': 'copyright_holder',
    'eBook ISBN': 'ebook_isbn',
    'DOI': 'doi',
    'Hardcover ISBN': 'hardcover_isbn',
    'Softcover ISBN': 'softcover_isbn',
    'SeriesISSN': 'series_issn',
    'EditionNumber': 'edition_number',
    'NumberofPages': 'page_num',
    'NumberofIllustrationsandTables': 'illu_table_num',
    'Topics': 'topics',
    'Authors': 'editors',
}
    
    
def springer(response):
    item = springerItem()
    for key in item.fields.keys():
        item[key] = ''
        
    for i in range(1,4):
        for i2 in range(1,10):
            key = response.xpath(
                '//div[@class="product-bibliographic"]/dl/dd/'\
                'div/div/dl[%s]/dt[%s]/text()' % (i, i2)
            ).extract_first()
            
            info = response.xpath(
                '//div[@class="product-bibliographic"]/dl/dd/'\
                'div/div/dl[%s]/dd[%s]/text()' % (i, i2)
            ).extract()
            
            if not key:
                continue
            
            if key=='Editors' or key=='Authors':
                info=';'.join(response.xpath(
                    '//div[@class="product-bibliographic"]/dl/dd/div/'\
                    'div/dl[%s]/dd[%s]/ul//span/text()' % (i, i2)
                    ).extract()
                )
            elif key=='Publisher':
                info = response.xpath(
                    '//div[@class="product-bibliographic"]/dl/dd/div/'\
                    'div/dl[%s]/dd[%s]/span/text()' % (i, i2)
                ).extract_first()
            elif key=='Topics':
                info=';'.join(response.xpath(
                    '//div[@class="product-bibliographic"]/dl/dd/div/'\
                    'div/dl[%s]/dd[%s]/ul/li/a/text()' % (i, i2)
                    ).extract()
                )
            elif info:
                info = info[0]

            if key in KEYS.keys():
                item[KEYS[key]] = str(info).strip('\n').strip(' ')
            item['url'] = response.url
            item['create_date'] = dt.today()
            item['file'] = response.meta['para']['file']

    yield item