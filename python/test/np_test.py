import numpy as np

a = np.array([2, 0, 1, 5])  # 创建数组
print(a)
print(a[:3])  # 切片前三个 a[:3] == a[0:3:1], 0和3为含头不含尾的索引，1为步长
print(a.min())
a.sort()
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b * b)
