#程序文件ti8_6.py
import sympy as sp

sp.var('h,g'); t=sp.Function('t')
eq=t(h).diff(h)-10000*sp.pi/sp.sqrt(2*g)*(h**sp.Rational(3,2)-
                                          2*h**sp.Rational(1,2))
ts=sp.dsolve(eq, ics={t(1): 0})
ts=sp.simplify(ts.args[1]); print(ts)
