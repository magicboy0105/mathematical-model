#程序文件ex17_3.py
import sympy as sp

sp.var('x,y')         #定义符号变量
f = sp.Function('f')  #定义符号函数
u = f(x,y); ux = u.diff(x); uy = u.diff(y)
eq = x*ux - y*uy + y**2*u - y**2
sp.pprint(eq)       #显示方程
s = sp.pdsolve(eq)  #求通解
sp.pprint(s)        #显示通解

