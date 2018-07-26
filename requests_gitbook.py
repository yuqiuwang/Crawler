# -*- coding: utf-8 -*-
"""
Author  : yuqiuwang
Mail    : yuqiuwang929@gmail.com
Created : 2018/7/26 11:19
"""

import requests
from lxml import etree
import threading
import time


# 使用了requests及lxml模块进行数据爬取
# threading模块进行多线程操作


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}


def crawler(my_url):
    response = requests.get(my_url, headers=headers)
    time.sleep(1)
    tree = etree.HTML(response.text)
    books = tree.xpath('//div[@class="book-infos"]/h2/a/text()')  # 书籍名称 XPATH
    links = tree.xpath('//div[@class="book-infos"]/h2/a//@href')  # 链接 XPATH
    with open("gitbook.txt", 'a+', encoding='utf8') as f:    # 多线程同时读写同一个文件有一定概率出问题，较重要的数据最好写入不同文件，再cat到一起
        for idx, book in enumerate(books):
            f.write(book+"\t"+links[idx]+"\n")


def multi_run(start_num, end_num):
    # 通过多线程爬取结果，提高效率
    threads = []
    for page_num in range(start_num, end_num):
        if page_num == 0:
            url = "https://legacy.gitbook.com/explore"
        else:
            url = "https://legacy.gitbook.com/explore?page=%d&lang=" % page_num
        t = threading.Thread(target=crawler, args=(url, ))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    total_page = 117563    # 总页数
    start_page = 0
    end_page = 50
    while end_page < total_page:    # 每一轮爬取50页
        print("Crawling page %d" % start_page)
        multi_run(start_page, end_page)
        print("%d page Crawling ok!" % (end_page-1))
        start_page += 50
        end_page += 50
    multi_run(start_page, total_page)
    print("%d page Crawling ok!" % total_page)
