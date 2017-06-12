#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    """
    使用pandas过滤数据
    """
    catering_sale = '../resources/chapter3/demo/data/catering_sale.xls'
    data = pd.read_excel(catering_sale, index_col=r'日期')
    data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)]  # 过滤异常数据
    statistics = data.describe()  # 保存基本统计量

    statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']  # 极差
    statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']  # 变异系数
    statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']  # 四分位数间距

    print(statistics)
