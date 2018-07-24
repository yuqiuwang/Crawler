# -*- coding: utf-8 -*-
"""
Author  : wangyuqiu
Mail    : yuqiuwang929@gmail.com
Created : 2018/7/12 14:31
"""

from selenium import webdriver
import time
import random


# 使用selenium爬取链家成都高新区二手房价信息
# 每一页爬取前，随机等待1~3s


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

def get_data(my_url, savefile):
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)
    driver = webdriver.Chrome("D:/chromedriver_win32/chromedriver.exe", chrome_options=chrome_options)
    #driver = webdriver.Chrome("D:/chromedriver_win32/chromedriver.exe")
    driver.get(my_url)
    contents = driver.find_elements_by_class_name("clear")
    for cont in contents:
        savefile.write(cont.text.replace("\n", "\t")+"\n")
    driver.quit()
    return savefile


f = open("cd_liangjia.xls", 'w+')
for x in range(1, 101):
    url = "https://cd.lianjia.com/ershoufang/gaoxin7/pg%d" % x
    f = get_data(url, f)
    print("第%d页，搞定了！" % x)
f.close()
