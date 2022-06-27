#程序文件ex2_50_2.py
import sympy as sp
x = sp.var('x:2')  #定义符号数组
s = sp.solve([x[0]**2+x[1]**2-1,x[0]-x[1]], x)
print(s)
