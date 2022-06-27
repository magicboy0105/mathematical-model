#程序文件ti15_2.py
import numpy as np
import sympy as sp

x0 = np.array([2.874, 3.278, 3.337, 3.390, 3.679])
n = len(x0); lamda = x0[:-1]/x0[1:]  #计算级比
b1 = [lamda.min(), lamda.max()]  #计算级比的范围
b2 = [np.exp(-2/(n+1)),np.exp(2/(n+1))]  #计算级比容许范围
x1=np.cumsum(x0); ax0 = np.diff(x0)    #计算累加和累减序列
z = 0.5*(x1[1:]+x1[:-1])  #计算均值生成序列
B = np.vstack([-x0[1:],-z,np.ones(n-1)]).T
u = np.linalg.pinv(B) @ ax0   #最小二乘法拟合参数
print("参数u：",np.round(u,4))
sp.var('t'); sp.var('x',cls=sp.Function)
eq = x(t).diff(t,2)+u[0]*x(t).diff(t)+u[1]*x(t)-u[2]
s = sp.dsolve(eq,ics={x(0):x0[0],x(4):x1[-1]})  #求微分方程符号解
xt=s.args[1]  #提取解的符号表达式
print('xt=',xt)
ft = sp.lambdify(t,xt,'numpy')  #转换为匿名函数
xh1 = ft(np.arange(n))  #求预测值
xh0 = np.hstack([x0[0],np.diff(xh1)])  #还原数据
e = x0-xh0             #计算已知数据预测的残差
delta = abs(e/x0)*100  #计算相对误差
rho=abs(1-(1-0.5*u[0])/(1+0.5*u[0])*lamda)  #计算级比偏差值
print('相对误差：',np.round(delta,4))

