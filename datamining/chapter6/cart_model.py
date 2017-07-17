"""
使用CART 决策树模型代码
"""
if __name__ == '__main__':
    import pandas as pd
    from random import shuffle
    import matplotlib.pyplot as plt

    data_file = '../resources/chapter6/demo/data/model.xls'
    data = pd.read_excel(data_file)
    data = data.as_matrix()
    shuffle(data)  # 打乱数据

    p = 0.8
    train = data[:int(len(data) * p)]  # 前80%为训练数据
    test = data[int(len(data) * p):]  # 后20%为测试集

    from sklearn.tree import DecisionTreeClassifier  # 导入决策树模型

    tree_file = './tmp/tree.pkl'  # 模型输出名字
    tree = DecisionTreeClassifier()  # 建立决策树模型
    tree.fit(train[:, :3], train[:, 3])  # 训练

    # 保存模型
    from sklearn.externals import joblib

    joblib.dump(tree, tree_file)

    from datamining.chapter5.cm_plot import *

    cm_plot(train[:, 3], tree.predict(train[:, :3])).show()

    from sklearn.metrics import roc_curve

    fpr, tpr, thresholds = roc_curve(test[:, 3], tree.predict(test[:, :3]), pos_label = 1)
    plt.plot(fpr, tpr, linewidth = 2, label = 'ROC of CART')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.ylim(0, 1.05)
    plt.xlim(0, 1.05)
    plt.legend(loc = 4)
    plt.show()
