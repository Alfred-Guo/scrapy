# -*- coding: utf-8 -*-
"""
@author: Alfred
"""
import random

from project.constants import USER_AGENT


class RandomProxy(object):
    """
    random pick a proxy through a file.
    """

    def __init__(self):
        fobj = open()
        self.proxies = [l.strip('\n') for l in fobj]
        fobj.close()

    def process_request(self, request, spider):
        """
        load the proxy.
        """

        if not self.proxies:
            return
        proxy = random.choice(self.proxies)
        print('Proxy:%s' %proxy)
        request.meta['proxy'] = "http://%s" % proxy


class RandomUserAgent(object):
    """
    random pick a user-agent through the user-agent dict.
    """

    def process_request(self, request, spider):
        """
        load the user-agent
        """

        agent = random.choice(USER_AGENT)
        request.headers.setdefault('User-Agent', agent)
