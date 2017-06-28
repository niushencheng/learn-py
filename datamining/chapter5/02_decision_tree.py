"""
决策树示例
"""
import pandas as pd

if __name__ == '__main__' :
    file_name = '../resources/chapter5/data/sales_data.xls'
    data = pd.read_excel(file_name, index_col = u'序号')

    data[data == u'好'] = 1
    data[data == u'是'] = 1
    data[data == u'高'] = 1
    data[data != 1] = -1

    x = data.iloc[:, :3].as_matrix().astype(int)
    y = data.iloc[:, :3].as_matrix().astype(int)

    from sklearn.tree import DecisionTreeClassifier as DTC

    dtc = DTC(criterion = 'entropy')  # 建立决策树模型，基于信息熵
    dtc.fit(x, y)

    from sklearn.tree import export_graphviz

    x = pd.DataFrame(x)
    with open("tree.dot", 'w') as f :
        f = export_graphviz(dtc, feature_names = x.columns, out_file = f)
