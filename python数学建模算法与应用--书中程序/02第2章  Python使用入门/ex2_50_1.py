#程序文件ex2_50_1.py
import sympy as sp
sp.var('x1,x2')
s=sp.solve([x1**2+x2**2-1,x1-x2],[x1,x2])
print(s)
