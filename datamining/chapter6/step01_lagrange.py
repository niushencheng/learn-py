"""
第一步：
    插值，补充缺少的数据
"""

import pandas as pd
from scipy.interpolate import lagrange


# s为列向量，n为要插值的位置，k为取前后数据的个数
def ployinterp_column(s, n, k = 5):
    values = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    values = values[values.notnull()]
    return lagrange(values.index, list(values))(n)


if __name__ == '__main__':
    input_file = '../resources/chapter6/demo/data/missing_data.xls'
    output_file = './solved_missing_data.xls'

    # 读取元素
    data = pd.read_excel(input_file, header = None)
    for i in data.columns:
        nulls = data[i].isnull()
        for j in range(len(data)):
            if nulls[j]:
                data[i][j] = ployinterp_column(data[i], j)

    data.to_excel(output_file, header = None, index = False)
