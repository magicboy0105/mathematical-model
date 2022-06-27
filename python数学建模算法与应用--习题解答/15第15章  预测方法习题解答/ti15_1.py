#程序文件ti15_1.py
import numpy as np
import sympy as sp

x0 = np.array([27260,29547,32411,35388])
n = len(x0); lamda = x0[:-1]/x0[1:]  #计算级比
b1 = [min(lamda), max(lamda)]  #计算级比取值范围
b2 = [np.exp(-2/(n+1)), np.exp(2/(n+1))]  #计算级比容许范围
x1 = np.cumsum(x0)  #求累加序列
z = (x1[:-1]+x1[1:]) / 2  #求均值生成序列
B = np.vstack([-z, np.ones(n-1)]).T
u = np.linalg.pinv(B) @ x0[1:]  #最小二乘法拟合参数
sp.var('t'); sp.var('x', cls=sp.Function)  #定义符号变量和函数
eq = x(t).diff(t)+u[0]*x(t)-u[1]  #定义符号微分方程
xt0 = sp.dsolve(eq, ics={x(0):x0[0]})  #求解符号微分方程
xt0 = xt0.args[1]  #提取方程中的符号解
xt = sp.lambdify(t, xt0, 'numpy')  #转换为匿名函数
t = np.arange(n+4); xh = xt(t)     #求预测值
x0h = np.hstack([x0[0], np.diff(xh)])  #还原数据
xf = x0h[-4:]  #提取预测值
cha = x0 - x0h[:-4]; delta = abs(cha/x0) * 100  #计算相对误差
rho = abs(1 - (1-0.5*u[0])/(1+0.5*u[0])*lamda)
print('预测值：', np.round(xf,4))
