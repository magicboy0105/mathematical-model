#程序文件ex2_45.py
from scipy.optimize import fsolve, root
fx = lambda x: [x[0]**2+x[1]**2-1, x[0]-x[1]]
s1 = fsolve(fx, [1, 1])
s2 = root(fx, [1, 1])
print(s1,'\n','--------------'); print(s2)
