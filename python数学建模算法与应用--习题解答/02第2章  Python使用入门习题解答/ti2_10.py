#程序文件ti2_10.py
import sympy as sp

sp.var('y')
f1 = sp.pi*(4-y**2); f2 = sp.pi*(4*y-y**2)
V = sp.integrate(f1, (y,-2,1)) + sp.integrate(f2, (y,1,3))
W = 1000*sp.Rational(98,10)*(sp.integrate(f1*(3-y),(y,-2,1))+
sp.integrate(f2*(3-y),(y,1,3)))
print(V); print(W)
