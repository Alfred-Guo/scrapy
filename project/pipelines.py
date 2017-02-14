# -*- coding: utf-8 -*-
"""
@author: Alfred
"""
import csv
from datetime import datetime as dt


class CsvPipeline(object):
    """
    Pipeline to csv file
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Get item fields and file path through crawler
        """

        path = crawler.settings.get('DATA_PATH')
        dir_name = crawler.settings.get('DIR_NAME')
        site = crawler.settings.get('SITE')

        flds = crawler.settings.get('CRAWL_DICT')['field_to_export']

        return cls(path, dir_name, site, flds)

    def __init__(self,path, dir_name, site, flds):
        self.flds = flds
        file_path = '%s/%s/%s_%s.csv' \
            % (path, dir_name, site, dt.today().strftime('%Y-%m-%d'))
        self.writer = csv.writer(open(file_path, 'a'))

    def process_item(self, item, spider):
        """
        write file
        """

        row = []
        for fld in self.flds:
            try:
                for i in ['\n', '\r', u'\xa0']:
                    item[fld] = item[fld].replace(i, '')
                row.append(item[fld].strip(' '))
            except:
                row.append(item[fld])
        self.writer.writerow(row)
