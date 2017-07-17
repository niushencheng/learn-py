"""
Series示例
"""

import pandas as pd

if __name__ == '__main__':
    s = pd.Series([1, 2, 3, 4, 5])
    print(s[[0, 2]])
