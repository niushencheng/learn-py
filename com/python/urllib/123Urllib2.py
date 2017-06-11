# -*- coding: utf-8 -*-
import os
import platform
import time

import urllib


# def clear():
#     '''该函数用于清屏'''
#     print(u'内容较多，显示3秒后翻页')
#     time.sleep(3)
#     OS = platform.system()
#     if (OS == u'Windows'):
#         os.system('cls')
#     else:
#         os.system("clear")
#

def linkBaidu():
    url = 'http://www.baidu.com'

    with urllib.urlopen(url, timeout=3) as response:
        print (response.geturl())
        print(response.read())


if __name__ == '__main__':
    linkBaidu()
