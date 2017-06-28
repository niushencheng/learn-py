"""
Logistic Regression
逻辑回归功能测试
"""

import pandas as pd

if __name__ == '__main__' :
    file_name = '../resources/chapter5/data/bankloan.xls'

    data = pd.read_excel(file_name)
    # 自变量数据选择前八项
    x = data.iloc[:, :8]
    # 因变量数据选择最后一项
    y = data.iloc[:, 8]

    from sklearn.linear_model import LogisticRegression as LR
    from sklearn.linear_model import RandomizedLogisticRegression as RLR

    rlr = RLR()  # 建立逻辑回归模型，筛选变量
    rlr.fit(x, y)  # 训练模型
    rlr.get_support()  # 获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数

    print(u'通过随机逻辑回归模型筛选特征结束')
    print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
    x = data[data.columns[rlr.get_support()]]

    lr = LR()  # 建立逻辑回归模型
    lr.fit(x, y)
    print(u'逻辑回归模型训练结束')
    print(u'模型的平均正确率为：%s' % lr.score(x, y))  # 给出模型的平均正确率
