#程序文件ex8_6.py
import sympy as sp

sp.var('t')
sp.var('x1:4', cls=sp.Function) #定义3个符号函数
x = sp.Matrix([x1(t), x2(t), x3(t)])  #列向量
A = sp.Matrix([[3,-1,1],[2,0,-1],[1,-1,2]])
eq = x.diff(t)-A@x
s = sp.dsolve(eq, ics={x1(0):1, x2(0):1, x3(0):1})
print(s)



