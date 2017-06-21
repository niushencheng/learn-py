#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import font_manager
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 餐饮菜品盈利数据
    dish_profit = '../resources/chapter3/demo/data/catering_dish_profit.xls'
    data = pd.read_excel(dish_profit, index_col=u'菜品名')
    data = data[u'盈利'].copy()
    data.sort_values(ascending=False)

    my_font = font_manager.FontProperties(fname='/Users/tinker/Downloads/bb4839/zh.ttf')
    # plt.rcParams['font.sans-serif'] = 'Bitstream Vera Sans'
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    data.plot(kind='bar')
    plt.ylabel(u'盈利(元)')
    # plt.ylabel(u'盈利(元)',fontproperties=my_font)
    p = 1.0 * data.cumsum() / data.sum()
    print(u'p type: %s ,p value: %s' % (type(p), p))
    p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
    plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6 * 0.9, p[6] * 0.9),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
    plt.ylabel(u'盈利(比例)')

    plt.show()
