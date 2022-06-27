#程序文件ex2_36.py
import numpy as np
a = np.eye(4)
b = np.rot90(a)
c, d = np.linalg.eig(b)
print('特征值为：', c)
print('特征向量为：\n', d)
