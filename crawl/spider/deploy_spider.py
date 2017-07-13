#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一键部署plus-beta环境
"""
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time, re


class DeployPlus(object):
    """
    部署类
    """

    def __init_property__(self, url, project_name, username, password):
        self.project_name = project_name
        self.username = username
        self.password = password
        self.br = self.__init_browser__(url)

    def __parse_file__(self, file_location):
        with open(file_location, encoding = 'utf-8') as fp:
            lines = fp.readlines()
            data = {}
            for line in lines:
                splits = line.strip().replace('\n', '').replace(' ', '').split('=')
                data[splits[0]] = splits[1]
        return data

    def __init_browser__(self, url):
        # 加载chrome
        br = webdriver.Chrome()

        # 设置超时时间
        br.set_page_load_timeout(10)
        br.set_script_timeout(5)
        br.get(url)
        return br

    def start_deploy(self, file_location):
        data = self.__parse_file__(file_location)
        self.__init_property__(data['url'], data['project'], data['username'], data['password'])
        self.__init_browser__(data['url'])
        br = self.br

        # 选取用户名密码
        time.sleep(5)
        pc_login = br.find_element_by_id('form-img')
        pc_login.click()
        username = br.find_element_by_id('login-username')
        username.send_keys(self.username)
        password = br.find_element_by_id('login-password')
        password.send_keys(self.password)
        commit = br.find_element_by_name('commit')
        commit.click()

        # 引入bs
        time.sleep(5)  # 休息5s，防止超时
        soup = bs(br.page_source, 'lxml')
        project_data_reactid = soup.find_all(text = re.compile(self.project_name))[0].parent['data-reactid']
        project = br.find_element_by_css_selector('[data-reactid="' + project_data_reactid + '"]')
        project.click()

        # 选中创建任务
        time.sleep(3)
        soup = bs(br.page_source, 'lxml')
        mission_data_reactid = soup.find_all(text = re.compile(r'创建任务'))[0].parent['data-reactid']
        create = br.find_element_by_css_selector('[data-reactid="' + mission_data_reactid + '"]')
        create.click()

        # 选中要发布的beta
        time.sleep(3)
        soup = bs(br.page_source, 'lxml')
        beta_data_reactid = soup.find_all(text = re.compile(r'^发布$'))[-2].parent['data-reactid']
        beta = br.find_element_by_css_selector('[data-reactid="' + beta_data_reactid + '"]')
        beta.click()

        # 选中所有机器
        time.sleep(3)
        machine_list = br.find_elements_by_css_selector('[type="checkbox"]')
        for i in machine_list:
            i.click()
        submit = br.find_element_by_css_selector('[type="submit"]')
        submit.click()
        time.sleep(3)
        br.quit()


if __name__ == '__main__':
    DeployPlus().start_deploy(file_location = '/data/paas-deploy.txt')
