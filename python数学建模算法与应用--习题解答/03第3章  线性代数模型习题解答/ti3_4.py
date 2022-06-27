#程序文件ti3_4.py
import sympy as sp
X=sp.Matrix(sp.var('x1:6')); sp.var('q')
A=sp.Matrix([[0, 1.8, 2.4, 2.0, 1.8],
             [q, 0, 0, 0, 0],[0, 0.98, 0, 0, 0],
             [0, 0, 0.95, 0, 0],[0, 0, 0, 0.80, 0]])
s = sp.solve([A@X-X,sum(X)-1])
print(s)


