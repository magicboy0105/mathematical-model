#程序文件ex16_3.py
import numpy as np
import sympy as sp

A = np.array([[3,1,1,1,1,-1],[1,3,1,1,-1,1],[1,-1,3,1,1,1],
    [-1,1,1,3,1,1],[1,1,-1,1,3,1],[1,1,1,-1,1,3]],dtype=int)
Az1 = np.hstack([A.T, -np.ones((6,1))])
Az2 = np.vstack([Az1, [1,1,1,1,1,1,0]])  #构造完整的系数阵
B = np.array([[0,0,0,0,0,0,1]]).T  #非线性方程组的常数项列
Az3 = np.hstack([Az2,B]) #构造增广阵
Az4 = sp.Matrix(Az3.astype(int))  #转换为符号矩阵
s1 = Az4.rref()  #把增广阵化成行最简形
s2 = np.linalg.pinv(Az2) @ B  #求最小范数解
print('行最简形为：\n',s1[0]); print('最小范数解为：\n',s2)
np.savetxt('data16_3.txt',A,fmt='%.0f')

