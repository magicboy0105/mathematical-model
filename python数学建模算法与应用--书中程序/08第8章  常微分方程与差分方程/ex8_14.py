#程序文件ex8_14.py
import numpy as np
t0=np.array([0,1,2,3,4,5,6,8,10,12,14,16,18])
x0=np.array([60,63,64,63,61,58,53,44,39,38,41,46,53])
y0=np.array([30,34,38,44,50,55,58,56,47,38,30,27,26])
dt=np.diff(t0); dx=np.diff(x0); dy=np.diff(y0)
temp=x0[:-1]*y0[:-1]
mat1=np.vstack([x0[:-1], -temp, np.zeros((2,12))]).T
mat2=np.vstack([np.zeros((2,12)), -y0[:-1], temp]).T
mat=np.vstack([mat1,mat2])  #构造线性方程组系数矩阵
b=np.hstack([dx/dt,dy/dt])  #构造线性方程组常数项列
cs=np.linalg.pinv(mat)@b    #线性最小二乘法拟合参数
print('参数a,b,c,d的值分别为:', np.round(cs,4))
