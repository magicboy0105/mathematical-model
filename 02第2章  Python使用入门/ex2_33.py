#程序文件ex2_33.py
import numpy as np
a = np.array([[0, 3, 4], [1, 6, 4]])
b = np.linalg.norm(a, axis=1)  #求行向量2范数
c = np.linalg.norm(a, axis=0)  #求列向量2范数
d = np.linalg.norm(a)   #求矩阵2范数
print('行向量2范数为：', np.round(b, 4))
print('列向量2范数为：', np.round(c, 4))
print('矩阵2范数为：', round(d, 4))
