#程序文件ex2_31.py
import numpy as np

a = np.array([[0, 3, 4], [1, 6, 4]])
b = np.array([[1, 2, 3], [2, 1, 4]])
c = a / b   #两个矩阵对应元素相除
d = np.array([2, 3, 2])
e = a * d   #d先广播成与a同维数的矩阵，再逐个元素相乘
f = np.array([[3],[2]])
g = a * f
h = a ** (1/2)  #a矩阵逐个元素的1/2次幂。
