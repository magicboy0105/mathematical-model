#程序文件ex2_47.py
from scipy.optimize import least_squares
import numpy as np
a=np.loadtxt('data2_47.txt')
x0=a[0]; y0=a[1]; d=a[2]
fx=lambda x: np.sqrt((x0-x[0])**2+(y0-x[1])**2)-d
s=least_squares(fx, np.random.rand(2))
print(s, '\n', '------------', '\n', s.x)
