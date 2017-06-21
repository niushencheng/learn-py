"""
数据规范化代码测试
"""
import pandas as pd
import numpy as np

"""
pd.read_excel(file_name, header=None)，的时候数据才会从头顶开始，
并不计算表头
     0    1    2     3
0   78  521  602  2863
1  144 -600 -521  2245
2   95 -457  468 -1283
3   69  596  695  1054
4  190  527  691  2051
5  101  403  470  2487
6  146  413  435  2571
"""
if __name__ == '__main__':
    data_file = '../resources/chapter4/demo/data/normalization_data.xls'
    data = pd.read_excel(data_file, header=None)

    print('origin data -->>')
    print(data)
    print('----------------------------------------------------------------')

    '''
    最小-最大规范化
    '''
    d1 = (data - data.min()) / (data.max() - data.min())
    print('d1-->>')
    print(d1)
    print('----------------------------------------------------------------')

    '''
    零-均值规范化
    '''
    d2 = (data - data.mean()) / data.std()
    print('d2-->>')
    print(d2)
    print('----------------------------------------------------------------')

    '''
    小数定标规范化
    '''
    d3 = data / (10 ** np.ceil(np.log10(data.abs().max())))
    print('d3-->>')
    print(d3)
    print('----------------------------------------------------------------')
