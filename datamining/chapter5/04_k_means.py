"""
K-Means聚类算法
"""
import pandas as pd


def density_plot(data):  # 自定义作图函数
    import matplotlib.pyplot as plt
    p = data.plt(kind = 'kde', linewidth = 2, subplots = True, sharex = False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.figure()
    return plt


if __name__ == '__main__':
    input_file = '../resources/chapter5/data/consumption_data.xls'
    k = 3  # 聚类的类别
    iteration = 500  # 聚类最大循环次数
    data = pd.read_excel(input_file, index_col = u'Id')
    data_sz = 1.0 * (data - data.mean()) / data.std()  # 数据标准化

    from sklearn.cluster import KMeans

    model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration)  # k类 ，4worker，500
    model.fit(data_sz)

    # 简单展示
    r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis = 1)  # 横向连接(0是纵向), 得到聚类中心对应的类别下的数目
    r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
    print(r)

    r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)
    r.columns = list(data.columns) + [u'类别']
    density_plot(data[r[u'类别'] == 1]).show()

