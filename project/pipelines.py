# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:01:10 2017
@author: Alfred
"""
import csv

#from utils.db_con import DBcon


class CsvPipeline():
    """
    Pipeline to csv file
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Get item fields and file path through crawler
        """
        return cls(crawler.settings)

    def __init__(self, settings):
        self.flds = settings.get('field_to_export')
        self.writer = csv.writer(
            open(settings['FILE_PATH'], 'a', encoding='utf-8', newline='')
        )

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


class SQLite3Pipeline():
    """
    1
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        1
        """
        return cls(crawler.settings)

    def __init__(self, settings):
        self.tbl = settings.get('TBL')
        self.db = DBcon()

    def process_item(self, item, spider):
        """
        write file
        """
        self.db.sqlite_insert(self.tbl, [item])
