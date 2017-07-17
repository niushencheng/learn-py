"""
使用神经网络预测销量高低
"""
if __name__ == '__main__':
    import pandas as pd

    # 读取数据
    file_name = '../resources/chapter5/data/sales_data.xls'
    data = pd.read_excel(file_name, index_col = u'序号')

    data[data == u'好'] = 1
    data[data == u'是'] = 1
    data[data == u'高'] = 1
    data[data != 1] = 0
    x = data.iloc[:, :3].as_matrix().astype(int)
    y = data.iloc[:, 3].as_matrix().astype(int)

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    model = Sequential()  # 建立模型
    model.add(Dense(input_dim = 3, output_dim = 10))
    model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅度提供准确度
    model.add(Dense(input_dim = 10, output_dim = 1))
    model.add(Activation('sigmoid'))  # 由于是0-1输出，用sigmoid函数作为激活函数

    model.compile(loss = 'binary_crossentropy', optimizer = 'adam')
    # 编译模型。由于使用二元分类，所以指定损失函数为binary_crossentropy，以及模式为binary
    # 另外常见的损失函数有mean_squared_error、categorical_crossentropy等
    model.fit(x, y, epochs = 1000, batch_size = 10)  # 训练模型，学习一千次
    yp = model.predict_classes(x).reshape(len(y))  # 分类预测

    from datamining.chapter5.cm_plot import *

    cm_plot(y, yp).show()
