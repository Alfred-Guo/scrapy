# -*- coding: utf-8 -*-
import csv
from datetime import datetime as dt

from project.setups import crawl_dict


class csvPipeline(object):
    
    @classmethod
    def from_crawler(cls, crawler):
        dir_name = crawler.settings.get('DIR_NAME')
        site = crawler.settings.get('SITE')
        path = crawler.settings.get('DATA_PATH')
        part = crawler.PART
        suf = crawler.SUF
        _file = crawler.settings.get('FILE_')
        return cls(dir_name, site, part, suf, path, _file)
      
    def __init__(self, dir_name, site, part, suf, path, _file):
        if _file:
            f = _file.split('#')
            self.writer = csv.writer(open(f[0], f[1]))
        elif suf!='':
            f = '%s/%s/%s_%s_%s_%s.csv' \
                % (path, dir_name, site, dt.today().strftime('%Y-%m-%d'), 
                   suf, part)
            self.writer = csv.writer(open(f, 'w'))
        else:
            f = '%s/%s/%s_%s_%s.csv' \
                % (path, dir_name, site, dt.today().strftime('%Y-%m-%d'), 
                   part)
            self.writer = csv.writer(open(f, 'w'))
        
    def process_item(self, item, spider):
        row = []
        for field in crawl_dict[spider.settings.get('DIR_NAME')]\
                                ['field_to_export']:
            try:
                for i in ['\n', '\r', u'\xa0']:
                    item[field] = item[field].replace(i, '')
                row.append(item[field].strip(' '))
            except:
                row.append(item[field])
        self.writer.writerow(row)