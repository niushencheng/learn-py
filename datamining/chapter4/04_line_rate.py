"""
线损率案例
"""

import pandas as pd

if __name__ == '__main__':
    input_file = '../resources/chapter4/demo/data/electricity_data.xls'
    data = pd.read_excel(input_file)
    # 线损率 = (供入电量 - 供出电量) / 供入电量 * 100%
    data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量']) / data[u'供入电量']

    print(data)
