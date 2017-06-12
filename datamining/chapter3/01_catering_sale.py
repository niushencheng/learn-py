import pandas as pd
import matplotlib.pyplot as plt  # 导入图像库

if __name__ == '__main__':
    """
    展示餐饮销额数据异常值检测代码
    """
    # 餐饮数据
    catering_sale = '../resources/chapter3/demo/data/catering_sale.xls'
    data = pd.read_excel(catering_sale, index_col=u'日期')
    # print(data.describe())
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure()  # 建立图像

    p = data.boxplot(return_type='dict')  # 画箱线图，直接使用DataFrame方法
    x = p['fliers'][0].get_xdata()  # fliers为异常值的标签
    y = p['fliers'][0].get_ydata()
    y.sort()  # 从小到大排序，该方法直接改变原对象

    # 用annotate添加注释
    for i in range(len(x)):
        if i > 0:
            plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
        else:
            plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

    plt.show()

"""
结合具体业务，可以将865、4060.3、4065.2归为正常值，
将22、51、60、6607.4、9106.44归为异常值
"""