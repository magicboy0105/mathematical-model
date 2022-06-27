#程序文件ex3_1_3.py
import sympy as sp

sp.var('k'); y = sp.Function('y')
f = y(k+2)-y(k+1)-y(k)
s = sp.rsolve(f, y(k),{y(0):1,y(1):1})
print(s) 

