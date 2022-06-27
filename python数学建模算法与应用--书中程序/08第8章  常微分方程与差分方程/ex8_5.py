#程序文件ex8_5.py
import sympy as sp

sp.var('t'); y=sp.Function('y')
u=sp.exp(-t)*sp.cos(t)
eq=y(t).diff(t,4)+10*y(t).diff(t,3)+35*y(t).diff(t,2)+\
    50*y(t).diff(t)+24*y(t)-u.diff(t,2)
con={y(0):0, y(t).diff(t).subs(t,0):-1,
     y(t).diff(t,2).subs(t,0):1, y(t).diff(t,3).subs(t,0):1}
s=sp.dsolve(eq, ics=con); s = sp.expand(s)
print(s); print('------'); print(s.args[1])



