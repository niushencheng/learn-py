#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver

br=webdriver.PhantomJS()
br.get('http://www.baidu.com')
br.implicitly_wait(10)
text_ele=br.find_element_by_id('kw')
text_ele.clear()
text_ele.send_keys('Python Selenium')

submit_ele = br.find_element_by_id('su')
submit_ele.click()

print(br.title)
