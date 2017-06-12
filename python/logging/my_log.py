#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    自定义日志模块
"""

__author__ = 'liangzicheng'
__version__ = '1.0.0'

import logging, getpass, sys


# define custom logging
class MyLog(object):
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

        # 日志文件名
        self.log_file = sys.argv[0][:-3] + '.log'
        self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s\r\n')

        # 日志显示到屏幕上并输出到日志文件内
        self.log_handler = logging.FileHandler(self.log_file, encoding='utf8')
        self.log_handler.setFormatter(self.formatter)
        self.log_handler.setLevel(logging.DEBUG)

        self.log_handler_st = logging.StreamHandler()
        self.log_handler_st.setFormatter(self.formatter)
        self.log_handler_st.setLevel(logging.DEBUG)

        self.logger.addHandler(self.log_handler)
        self.logger.addHandler(self.log_handler_st)

    # 日志的五个级别对应以下函数
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    my_log = MyLog()
    my_log.debug('my debug msg!')
    my_log.info('my info msg!')
    my_log.warn('my warn msg!')
    my_log.error('my error msg!')
    my_log.critical('my critical msg!')

