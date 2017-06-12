#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    beautiful-soup study
    used for crawl tie ba communicate info
"""

import string
from urllib import request, parse
from bs4 import BeautifulSoup as bs
from python.logging.my_log import MyLog


class Item(object):
    title = None  # 标题
    first_author = None  # 帖子创建者
    first_time = None  # 帖子创建时间
    re_num = None  # 回复总数
    content = None  # 最后回复内容
    last_author = None  # 最后回复者
    last_time = None  # 最新回复时间


class GetTieBaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = MyLog()
        self.page_sum = 5
        self.urls = self.get_urls(self.page_sum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def get_urls(self, page_sum):
        urls = []
        pns = [str(i * 50) for i in range(page_sum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info(u'获取urls信息成功！')
        return urls

    def spider(self, urls):
        items = []
        for url in urls:
            html_content = self.get_html_content(url)
            soup = bs(html_content, 'lxml')
            tagli = soup.find_all('li', {'class': ' j_thread_list clearfix'})
            for tag in tagli:
                item = Item()
                item.title = tag.find('a', {'class': 'j_th_tit'}).get_text().strip()
                item.first_author = tag.find('span', {'class': 'frs-author-name-wrap'}).a.get_text().strip()
                item.first_time = tag.find('span', {'title': u'创建时间'.encode('utf8')}).get_text().strip()
                item.re_num = tag.find('span', {'title': u'回复'.encode('utf8')})
                item.content = tag.find('div', {'class': 'threadlist_abs threadlist_abs_onlyline '}).get_text().strip()
                items.append(item)
        return items

    def pipelines(self, items):
        for item in items:
            print('item title : %s' % item.title)

    def get_html_content(self, url):
        """
        获取html内容
        :param url:
        :return:
        """
        try:
            # 将中文编码
            url = parse.quote(url, safe=string.printable)
            resp = request.urlopen(url)
        except Exception as e:
            self.log.error(u'请求 %s 连接时发生异常信息' % url)
            print(e)
        else:
            self.log.info(u'请求 %s 成功返回数据' % url)
            return resp.read()


if __name__ == '__main__':
    url = u'http://tieba.baidu.com/f?kw=权利的游戏&ie=utf-8&pn=0'
    res = GetTieBaInfo(url)
