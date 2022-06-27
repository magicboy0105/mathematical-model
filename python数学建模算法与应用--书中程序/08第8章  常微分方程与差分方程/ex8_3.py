#程序文件ex8_3.py
import sympy as sp

sp.var('x'); y=sp.Function('y')
eq=y(x).diff(x)+2*y(x)-2*x**2-2*x
s=sp.dsolve(eq, ics={y(0):1})
s=sp.simplify(s); print(s)
