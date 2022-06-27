#程序文件名ex7_18.py
import sympy as sp
sp.var('x')
base = sp.Matrix([1, x**2, x**4])  #列向量
y1 = base @ (base.T)
y2 = sp.cos(x) * base  #列向量
r1 = sp.integrate(y1, (x, -sp.pi/2, sp.pi/2))
r2 = sp.integrate(y2, (x, -sp.pi/2, sp.pi/2))
a = r1.inv() @ r2
xs = a.n(4)  #把符号数转换为小数
print('系数的符号解：\n', a)
print('系数的小数显示：', xs)
