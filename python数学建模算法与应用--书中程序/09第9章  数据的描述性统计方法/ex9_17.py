#程序文件ex9_17.py
import scipy.stats as ss
import numpy as np

f = open('data9_17.txt')
d = f.readlines(); a = []
for e in d: a.extend(e.split())
b = np.array([eval(e) for e in a])
xb = b.mean(); s = b.std(ddof=1)
st, p = ss.kstest(b, 'norm', (xb, s))
print('统计量：', round(st,4)); print('p值', round(p,4))
