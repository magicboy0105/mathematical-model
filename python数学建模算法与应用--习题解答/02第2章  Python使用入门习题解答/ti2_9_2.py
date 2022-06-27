#程序文件ti2_9_2.py
from scipy.optimize import fsolve
import numpy as np

fxy=lambda x:[x[0]**2-x[1]-x[0]-3,x[0]+3*x[1]-2]
s=fsolve(fxy,np.random.randn(2))
print('求得的一组数值解：', np.round(s,4))
