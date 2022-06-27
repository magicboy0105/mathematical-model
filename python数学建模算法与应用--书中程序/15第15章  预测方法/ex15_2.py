#程序文件ex15_2.py
import numpy as np
import sympy as sp

x0 = np.array([41,49,61,78,96,104])  #原始序列
n = len(x0); x1 = np.cumsum(x0)  #计算1次累加序列
ax0 = np.diff(x0)  #计算1次累减序列
z = (x1[1:]+x1[:-1])/2  #计算均值生成序列
B = np.vstack([-x0[1:], -z, np.ones(n-1)]).T
u = np.linalg.pinv(B) @ ax0
sp.var('t'); sp.var('x', cls=sp.Function)  #定义符号变量和函数
eq = x(t).diff(t,2)+u[0]*x(t).diff(t)+u[1]*x(t)-u[2]
s = sp.dsolve(eq, ics={x(0):x1[0], x(5):x1[-1]})  #求微分方程符号解
xt = s.args[1]  #提取解的符号表达式
x = sp.lambdify(t, xt, 'numpy')  #转换为匿名函数
xh1 = x(np.arange(n))  #求预测值
xh0 = np.hstack([x0[0], np.diff(xh1)])  #还原数据
ea = x0 - xh0  #计算预测的残差
er = abs(ea)/x0*100  #计算相对误差
print('参数u：', np.round(u,4))



