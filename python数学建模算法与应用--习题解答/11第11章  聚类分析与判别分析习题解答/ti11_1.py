#程序文件ti11_1.py
import numpy as np
import pylab as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import KMeans

a=np.loadtxt('ti11_1.txt')
z=sch.linkage(a,method='complete',metric='mahalanobis')
sch.dendrogram(z, labels=np.arange(1,18))

b=(a-a.min(axis=0))/(a.max(axis=0)-a.min(axis=0))
SSE=[]; K=np.arange(1,9)
for i in K:
    md=KMeans(i).fit(b)
    SSE.append(md.inertia_)
plt.figure(2); plt.plot(K, SSE, '*-'); plt.show()
md4=KMeans(4).fit(b)  #聚类成4类
labels=md4.labels_+1  #提取聚类标签
print('聚类结果为：', labels)
for i in range(1,5):
    print(i,'类：', np.where(labels==i)[0]+1)



