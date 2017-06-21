"""
拉格朗日插值
"""
import pandas as pd
from scipy.interpolate import lagrange


def predict_insert(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    print("type y : %s" % type(y))
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


if __name__ == '__main__':
    # 设置原始数据文件目录
    input_file = '../resources/chapter3/demo/data/catering_sale.xls'

    # 读取数据文件
    data = pd.read_excel(input_file)
    # 根据之前boxplot分析的结果，认为销量 < 400 | 销量 > 5000 的为异常数据，暂时清空
    data.ix[(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None

    for i in range(len(data[u'销量'])):
        if data[u'销量'].isnull()[i]:
            data[u'销量'][i] = predict_insert(data[u'销量'], i)

    data.to_excel('test.xls')
