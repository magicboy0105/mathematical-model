#程序文件ex2_28.py
import numpy as np
a = np.arange(16).reshape(4,4)  #生成4行4列的数组
b = np.floor(5*np.random.random((2, 4)))
c = np.ceil(6*np.random.random((4, 2)))
d = np.vstack([a, b])  #上下合并矩阵
e = np.hstack([a, c])  #左右合并矩阵
