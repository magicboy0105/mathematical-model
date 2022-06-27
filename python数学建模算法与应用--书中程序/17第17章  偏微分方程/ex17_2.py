#程序文件ex17_2.py
import sympy as sp

sp.var('f,G', cls=sp.Function)  #定义符号函数
sp.var('x,y,a,b,c')   #定义符号变量
u = f(x,y); ux = u.diff(x); uy = u.diff(y)
eq = a*ux + b*uy + c*u - G(x,y)
sp.pprint(eq)       #显示方程
s = sp.pdsolve(eq)  #求通解
sp.pprint(s)        #显示通解

