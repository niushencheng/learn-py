"""
离散点检测
"""
# 使用K-Means算法聚类消费行为特征数据

import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 参数初始化
    input_file = '../resources/chapter5/data/consumption_data.xls'
    k = 3  # 聚类的类别
    threshold = 2  # 离散点阈值
    iteration = 500  # 聚类的最大循环次数
    data = pd.read_excel(input_file, index_col = 'Id')
    data_zs = 1.0 * (data - data.mean()) / data.std()  # 数据标准化

    from sklearn.cluster import KMeans

    model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration)  # 分为k类，并发数4
    model.fit(data_zs)  # 开始聚类

    # 标准化数据及其类别
    r = pd.concat([data_zs, pd.Series(model.labels_, index = data.index)], axis = 1)
    # 重命令表头
    r.columns = list(data.columns) + [u'聚类类别']

    norm = []
    for i in range(k):
        norm_tmp = r[['R', 'F', 'M']][r[u'聚类类别'] == i] - model.cluster_centers_[i]
        norm_tmp = norm_tmp.apply(np.linalg.norm, axis = 1)  # 求出绝对距离
        norm.append(norm_tmp / norm_tmp.median())  # 求出相对距离并且添加

    norm = pd.concat(norm)  # 合并，type -->> Series

    import matplotlib.pyplot as plt

    # plt.rcParams['font.sans-serif'] = ['DejaVu Serif']
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    norm[norm <= threshold].plot(style = 'go')  # 正常点

    discrete_points = norm[norm > threshold]  # 离群点
    discrete_points.plot(style = 'ro')

    for i in range(len(discrete_points)):  # 离群点做标记
        id = discrete_points.index[i]
        n = discrete_points.iloc[i]
        plt.annotate('(%s, %0.2f)' % (id, n), xy = (id, n), xytext = (id, n))

    plt.xlabel(u'编号')
    plt.ylabel(u'相对距离')
    plt.show()
    import matplotlib

    print(matplotlib.matplotlib_fname())
