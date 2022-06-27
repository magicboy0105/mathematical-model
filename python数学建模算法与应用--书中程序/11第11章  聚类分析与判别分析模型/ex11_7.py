#程序文件ex11_7.py
import numpy as np
from sklearn.cluster import KMeans
import pylab as plt
from sklearn.metrics import silhouette_score

a = np.loadtxt('data11_2.txt')
b=(a-a.min(axis=0))/(a.max(axis=0)-a.min(axis=0))
S = []; K = range(2, len(a))
for i in K:
    md = KMeans(i).fit(b)
    labels = md.labels_
    S.append(silhouette_score(b, labels))
plt.plot(K, S,'*-'); plt.show()

