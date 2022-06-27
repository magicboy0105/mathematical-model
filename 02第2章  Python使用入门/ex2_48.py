#程序文件ex2_48.py
from scipy.sparse.linalg import eigs
import numpy as np

a = np.array([[1, 2, 3], [2, 1, 3], [3, 3, 6]], dtype=float)  #必须加float,否则出错
b, c = np.linalg.eig(a)
d, e = eigs(a, 1)
print('最大模特征值为：', d)
print('对应的特征向量为：\n', e)
