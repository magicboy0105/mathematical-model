#程序文件ex3_1_2.py
import sympy as sp

sp.var('t, c1, c2')
t0 = sp.solve(t**2-t-1)  #求解特征方程
eq1 = c1 + c2 - 1
eq2 = c1 * t0[0] + c2 *t0[1] - 1
s = sp.solve([eq1, eq2])
print('c1=', s[c1]); print('c2=', s[c2])

