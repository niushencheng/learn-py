"""
Apriori算法调用代码
"""

if __name__ == '__main__':
    import pandas as pd
    from datamining.chapter5.apriorilib import *

    input_file = '../resources/chapter5/data/menu_orders.xls'
    data = pd.read_excel(input_file, header = None)

    print(u'\n转换原始数据至0-1矩阵...')
    ct = lambda x: pd.Series(1, index = x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数
    b = map(ct, data.as_matrix())  # 用map方式执行
    data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用0填充
    print(u'\n转换完毕。')
    del b  # 删除中间变量b，节省内存

    support = 0.2  # 最小支持度
    confidence = 0.5  # 最小置信度
    ms = '---'  # 连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

    find_rule(data, support, confidence, ms)  # 保存结果
