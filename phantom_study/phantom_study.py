#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用selenium + phantomjs模拟百度搜索python selenium
"""
from selenium import webdriver

__author__ = 'niushencheng.com'
__version__ = '1.0.0'

if __name__ == '__main__':
    browser = webdriver.PhantomJS()
    browser.get('http://www.baidu.com')
    browser.implicitly_wait(10)

    # 拿到搜索框
    text_element = browser.find_element_by_id('kw')
    text_element.clear()
    text_element.send_keys('Python Selenium')

    # 模拟人工点击
    submit_element = browser.find_element_by_id('su')
    submit_element.click()

    print(browser.title)

