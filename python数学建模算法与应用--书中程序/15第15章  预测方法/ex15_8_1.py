#程序文件ex15_8_1.py
import numpy as np
import sympy as sp

p = np.array([[0.8, 0.1, 0.1],[0.5, 0.1, 0.4],[0.5, 0.3, 0.2]])
a = np.vstack([p.T-np.eye(3), np.ones(3)])  #构造方程组系数矩阵 
b = np.hstack([np.zeros(3),1])  #构造方程组常数项列
x = np.linalg.pinv(a) @ b  #求线性方程组的数值解
print('解为：', np.round(x,4))
