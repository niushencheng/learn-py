import pandas as pd

if __name__ == '__main__':
    # 餐饮数据，含有其他属性
    catering_sale = '../../datamining/resources/chapter3/demo/data/catering_sale_all.xls'
    # 读取数据，指定日期为索引列
    data = pd.read_excel(catering_sale, index_col=u'日期')
    # 相关系数矩阵
    # data.corr()
    # print(data.corr()[u'百合酱蒸凤爪'][u'翡翠蒸香茜饺'])
    # print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))
    print(data.loc[u'百合酱蒸凤爪'])
    # print(data.mean())