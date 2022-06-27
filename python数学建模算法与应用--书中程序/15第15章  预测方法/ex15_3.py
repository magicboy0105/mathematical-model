#程序文件ex15_3.py
import numpy as np
import sympy as sp

x0 = np.array([2.874,3.278,3.39,3.679,3.77,3.8])  #原始序列
n = len(x0); ax0 = np.diff(x0)  #计算1次累减序列
B = np.vstack([-x0[1:], np.ones(n-1)]).T
u = np.linalg.pinv(B) @ ax0  #最小二乘法拟合参数
sp.var('t'); sp.var('x', cls=sp.Function)  #定义符号变量和函数
eq = x(t).diff(t,2)+u[0]*x(t).diff(t)-u[1]
s = sp.dsolve(eq, ics={x(0):x0[0], x(t).diff(t).subs(t,0):x0[0]})
xt = s.args[1]  #提取解的符号表达式
x = sp.lambdify(t, xt, 'numpy')  #转换为匿名函数
xh1 = x(np.arange(n))  #求预测值
xh0 = np.hstack([x0[0], np.diff(xh1)])  #还原数据
ea = x0 - xh0  #计算预测的残差
er = abs(ea)/x0*100  #计算相对误差
print('参数u：', np.round(u,4))



