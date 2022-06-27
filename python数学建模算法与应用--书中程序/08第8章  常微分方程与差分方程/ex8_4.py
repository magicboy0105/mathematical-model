#程序文件ex8_4.py
import sympy as sp

sp.var('x'); y=sp.Function('y')
eq=y(x).diff(x,2)-2*y(x).diff(x)+y(x)-sp.exp(x)
con={y(0): 1, y(x).diff(x).subs(x,0): -1}
s=sp.dsolve(eq, ics=con); print(s)


