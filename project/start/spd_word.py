# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:10:10 2016
@author: Alfred
"""
import os

from spd import Spd


def word(response):
    item = {}
    item['word'] = os.path.basename(response.url)
    item['url'] = response.url

    for i in response.xpath(
            '//div[@class="entry-body__el clrd js-share-holder"]'
        ):
        # type
        item['type'] = i.xpath(
            './/h2//span[@class="pos"]/text()'
        ).extract_first()

        # ipa
        item['ipa'] = i.xpath(
            'string(.//span[@class="ipa"])'
        ).extract_first().replace('.', '')

        #v voice
        mp3 = i.xpath('.//span/@data-src-mp3').extract_first()
        ogg = i.xpath('.//span/@data-src-ogg').extract_first()
        item['voice'] = ';'.join([mp3, ogg])

        # meaning
        egs = i.xpath(
            'string(.//p[@class="def-head semi-flush"])'
        ).extract()
        trans = i.xpath(
            './/span[@class="def-body"]/span[@class="trans"]/text()'
        ).extract()
        for i in ['\n', '\t']:
            trans = [i2.replace(i, '') for i2 in trans]
        trans = [i.strip(' ') for i in trans]
        item['meaning'] = ';'.join([str(i) for i in zip(egs, trans)])

        # example
        examples = response.xpath('.//div[@class="examp emphasized"]')
        egs = [
            i.xpath('string(./span[@class="eg"])').extract_first()
            for i in examples
        ]
        trans = [
            i.xpath('string(./span[@class="trans"])').extract_first()
            for i in examples
        ]
        for i in ['\n', '\t']:
            trans = [i2.replace(i, '') for i2 in trans]
        trans = [i.strip(' ') for i in trans]
        item['example'] = ';'.join([str(i) for i in zip(egs, trans)])

        yield item


class Word(Spd):
    """
    springer spider
    """

    def __init__(self):
        custome_settings={
            'DIR_NAME': 'springer',
            'SITE': 'springer',
            'field_to_export': [
                'word', 'type', 'ipa', 'voice', 'meaning', 'example',
                'url',
            ],
            'CALLBACK': 'word',
            'PARSE': {'word': word},
        }
        super(Word, self).__init__(custome_settings)

    @staticmethod
    def get_urls():
        """
        generate the book url to crawl
        """
        url = 'http://dictionary.cambridge.org/dictionary/'\
            'english-chinese-simplified/%s'
        with open(r'C:\Users\Alfred\Documents\Python\My\scrapy\project\start\word.txt') as fobj:
            return [(url % i.strip('\n'), {}) for i in fobj]


if __name__ == '__main__':
    WORD = Word()
    WORD.start_crawl()
