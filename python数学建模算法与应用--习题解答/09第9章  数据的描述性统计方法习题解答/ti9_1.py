#程序文件ti9_1.py
import numpy as np
from scipy.stats import t

x0 = np.array([1050,1100,1120,1250,1280])
n = len(x0); alpha = 0.1
T = t.ppf(1-alpha/2, n-1)  #计算上alpha/2分位数
xb = x0.mean(); s = x0.std(ddof=1)
print('置信区间为({},{})'.format(xb-s/np.sqrt(n)*T,xb+s/np.sqrt(n)*T))
