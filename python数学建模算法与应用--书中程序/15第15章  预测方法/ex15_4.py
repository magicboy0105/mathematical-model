#程序文件ex15_4.py
import numpy as np

x0 = np.array([4.93, 2.33, 3.87, 4.35, 6.63, 7.15, 5.37, 6.39, 7.81, 8.35])
n = len(x0); x1 = np.cumsum(x0)  #求累加序列
z = (x1[1:]+x1[:-1]) / 2  #求均值生成序列
B = np.vstack([-z, z**2]).T
u = np.linalg.pinv(B) @ x0[1:]  #最小二乘法拟合参数
print('参数u：', np.round(u,4))
#下面直接利用解的表达式写出对应的匿名函数
x = lambda t: u[0]*x0[0]/(u[1]*x0[0]+(u[0]-u[1]*x0[0])*np.exp(u[0]*t))
xh1 = x(np.arange(n))  #求预测值
xh0 = np.hstack([x0[0], np.diff(xh1)])  #还原数据
ea = x0 - xh0  #计算预测的残差
er = abs(ea)/x0*100  #计算相对误差



