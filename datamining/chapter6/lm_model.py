"""
使用LM模型对原始数据分析
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

    # LM神经网络代码
    from keras.models import Sequential  # 导入神经网络的初始化函数
    from keras.layers.core import Dense, Activation  # 导入神经网络层函数、激活函数

    net_file = './tmp/net.model'  # 构建的神经网络模型的存储路径

    net = Sequential()  # 建立神经网络
    net.add(Dense(input_dim = 3, output_dim = 10))  # 添加输入层(3节点) 到隐藏层(10节点)的连接
    net.add(Activation('relu'))  # 隐藏层使用relu激活函数
    net.add(Dense(input_dim = 10, output_dim = 1))  # 添加隐藏层(10节点) 到输出层(1节点)的连接
    net.add(Activation('sigmoid'))  # 输出层使用sigmoid激活函数
    # 编译模型，使用adam方法求解
    net.compile(loss = 'binary_crossentropy', optimizer = 'adam')

    net.fit(train[:, :3], train[:, 3], nb_epoch = 10, batch_size = 1)  # 训练模型循环1000次
    net.save_weights(net_file)  # 保存模型

    predict_result = net.predict_classes(train[:, :3]).reshape(len(train))  # 预测结果变形

    from datamining.chapter5.cm_plot import *

    cm_plot(train[:, 3], predict_result).show()

    from sklearn.metrics import roc_curve  # 导入ROC曲线函数

    predict_result = net.predict_classes(test[:, :3]).reshape(len(test))  # 预测结果变形
    fpr, tpr, thresholds = roc_curve(test[:, 3], predict_result, pos_label = 1)
    plt.plot(fpr, tpr, linewidth = 2, label = 'ROC of LM')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.ylim(0, 1.05)
    plt.xlim(0, 1.05)
    plt.legend(loc = 4)
    plt.show()
