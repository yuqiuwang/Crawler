# -*- coding: utf-8 -*-
"""
Author  : yuqiuwang
Mail    : yuqiuwang929@gmail.com
Website : www.yuqiulearn.cn
Created : 2018/9/20 14:10
"""

from selenium import webdriver
# import time

my_url = 'https://www.baidu.com'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("D:/chromedriver_win32/chromedriver.exe", chrome_options=chrome_options)
driver.get(my_url)

contents = driver.find_element_by_xpath('//*[@name="wd"]')
contents.send_keys("test")
contents = driver.find_element_by_xpath('//*[@id="su"]')
contents.click()
