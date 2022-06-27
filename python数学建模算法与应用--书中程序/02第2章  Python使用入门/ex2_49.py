#程序文件ex2_49.py
import sympy as sp
a, b, c, x=sp.symbols('a,b,c,x')
x0=sp.solve(a*x**2+b*x+c, x)
print(x0)
