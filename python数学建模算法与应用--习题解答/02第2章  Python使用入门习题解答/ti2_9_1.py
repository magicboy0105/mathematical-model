#程序文件ti2_9_1.py
import sympy as sp

sp.var('x,y')
s=sp.solve([x**2-y-x-3,x+3*y-2])
print(s)
