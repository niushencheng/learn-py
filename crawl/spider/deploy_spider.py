#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一键部署plus-beta环境
"""

from selenium import webdriver
import time

if __name__ == '__main__' :
    br = webdriver.Chrome()

    # 设置超时时间
    br.set_page_load_timeout(10)
    br.set_script_timeout(5)
    br.get('http://plus.sankuai.com')

    time.sleep(5)
    pc_login = br.find_element_by_id('form-img')
    pc_login.click()
    username = br.find_element_by_id('login-username')
    username.send_keys('liangzicheng')
    password = br.find_element_by_id('login-password')
    password.send_keys('Liangzc2017')
    commit = br.find_element_by_name('commit')
    commit.click()

    time.sleep(5)
    projects = br.find_elements_by_class_name('project-info-list')
    project = projects[0]
    project.click()

    time.sleep(3)
    create = br.find_element_by_css_selector('[data-reactid=".1.1.1.0.0.0.0.1.0.$create"]')
    create.click()
    time.sleep(3)
    beta = br.find_element_by_css_selector('[data-reactid=".1.1.1.0.0.0.1.0.0.0.1.3.$3.2.1"]')
    beta.click()
    time.sleep(3)
    mechine = br.find_element_by_css_selector('[data-reactid=".1.1.1.0.0.0.1.0.0.2.0.2.4.2.2.1.$0.0.0"]')
    mechine.click()
    submit = br.find_element_by_css_selector('[data-reactid=".1.1.1.0.0.0.1.0.0.2.0.4.0"]')
    submit.click()
    time.sleep(3)
    br.quit()
