# -*- coding: utf-8 -*-
"""
Author  : yuqiuwang
Mail    : yuqiuwang929@gmail.com
Created : 2018/7/26 14:32
"""

import requests
from lxml import etree
import re


class ProxiesGet:
    """
    ----------------------------------------------------------------------
    #
    # 定义了一个在线获取高匿IP的类
    # proxies = ProxiesGet(需要获取IP网站的页数, 用于测试IP的链接)()
    # 主要用于提供爬虫脚本有效的IP地址
    #
    ----------------------------------------------------------------------
    # 通过爬虫脚本调用
    #
    # i.e.
    #   import proxies
    #   IPs = proxies.ProxiesGet(1, "http://www.baidu.com")()
    #
    # 返回list
    #
    # i.e.
    #   ["http://101.236.18.101:8866","http://101.236.60.48:8866"...]
    ----------------------------------------------------------------------
    """

    def __init__(self, page_nums, test_url):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            }
        self.page_nums = page_nums
        self.test_url = test_url

    def __call__(self):
        proxies = self.get_proxies()
        return self.test_proxies(self.test_url, proxies)

    def get_proxies(self):
        # 传入需要爬取的IP页数，一页约80个IP
        proxies = []
        for page_num in range(0, self.page_nums):
            response = requests.get("http://www.xicidaili.com/nn/%s" % (page_num+1), headers=self.header)
            tree = etree.HTML(response.text)
            table = tree.xpath('//table[@id="ip_list"]/tr/td/text()')
            proxies = re.findall(r'(\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}:\d+)', ":".join(table))
            proxies += proxies
        proxies = ["http://"+proxy for proxy in proxies]
        return proxies

    def test_proxies(self, test_url, proxies):
        # 测试IP是否可用，若不可用则剔除
        failed_proxies = []
        for proxy in proxies:
            try:
                response = requests.get(test_url, headers=self.header, proxies={"http": proxy})
                response.text
                print(proxy+"  Connection success!")
            except:
                print(proxy+"  Connection failed!")
                failed_proxies.append(proxy)
        for proxy in failed_proxies:
            proxies.pop(proxies.index(proxy))
        return proxies
