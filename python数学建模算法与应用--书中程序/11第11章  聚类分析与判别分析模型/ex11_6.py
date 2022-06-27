#程序文件ex11_6.py
import numpy as np
from sklearn.cluster import KMeans
import pylab as plt

a = np.loadtxt('data11_2.txt')
b=(a-a.min(axis=0))/(a.max(axis=0)-a.min(axis=0))
SSE = []; K = range(2, len(a)+1)
for i in K:
    md = KMeans(i).fit(b)
    SSE.append(md.inertia_)
plt.plot(K, SSE,'*-'); plt.show()

