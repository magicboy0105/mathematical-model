#程序文件ti2_11.py
from scipy.optimize import fsolve
import numpy as np

f=lambda x: (abs(x+1)-abs(x-1))/2+np.sin(x)
g=lambda x: (abs(x+3)-abs(x-3))/2+np.cos(x)
eqs=lambda z: [3*f(z[2])+4*g(z[3])-1-2*z[0],
               2*f(z[2])+6*g(z[3])-2-3*z[1],
               f(z[0])+3*g(z[1])-3-z[2],
               4*f(z[0])+6*g(z[1])-1-5*z[3]]
s=fsolve(eqs, np.random.randn(4))
print(s)
