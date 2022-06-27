#程序文件ex9_13.py
import numpy as np
from scipy.stats import t
from statsmodels.stats.weightstats import ztest

a = np.loadtxt('data9_13.txt').flatten()
xb = a.mean(); s = a.std(ddof=1)
n = len(a); ta = t.ppf(0.95, n-1)
ts, p = ztest(a, value=225, alternative='larger')
print('t统计量值：', ts)



             

     




