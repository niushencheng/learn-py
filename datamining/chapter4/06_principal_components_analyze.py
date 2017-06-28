"""
主成分分析代码
"""
import pandas as pd

if __name__ == '__main__' :
    input_file = '../resources/chapter4/demo/data/principal_component.xls'
    data = pd.read_excel(input_file)

    from sklearn.decomposition import PCA

    pca = PCA()
    pca.fit(data)

    # 返回模型的各个特征向量
    print(pca.components_)

    print('--------------------------------------')
    # 返回各个成分的各自的方差百分比
    print(pca.explained_variance_ratio_)
