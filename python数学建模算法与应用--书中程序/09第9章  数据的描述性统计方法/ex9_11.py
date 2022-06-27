#程序文件ex9_11.py
import numpy as np
from scipy.stats import t, sem

d = np.loadtxt('data9_11.txt')
d = d.flatten(); n = len(d)
xb = d.mean(); s = d.std(ddof=1)  #计算均值和标准差
sm = sem(d)  #计算样本均值的标准误差
a = 0.05; ta = t.ppf(1-a/2, n-1)
L = [xb-sm*ta, xb+sm*ta]
print(np.round(L, 4))

     
     




