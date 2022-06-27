#程序文件ti3_2.py
import sympy as sp
sp.var('n'); x = sp.Function('x')
f = x(n+2)-x(n+1)-2*x(n)
s = sp.rsolve(f,x(n),{x(0):-2,x(1):-2})
print(s)
