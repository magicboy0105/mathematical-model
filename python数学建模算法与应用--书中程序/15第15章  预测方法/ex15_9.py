#程序文件ex15_9.py
import numpy as np

p = np.array([[0.2, 0.8, 0],[0.8, 0, 0.2],[0.1, 0.3, 0.6]])
a = np.vstack([p.T-np.eye(3), np.ones((1,3))])  #构造方程组系数矩阵 
b = np.hstack([np.zeros(3),1])  #构造方程组常数项列
x = np.linalg.pinv(a) @ b       #求线性方程组的数值解
print('解为：', np.round(x,4))
