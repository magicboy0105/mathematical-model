#程序文件ti11_2.py
import numpy as np
import pylab as plt
import scipy.cluster.hierarchy as sch
from scipy.stats import zscore

a=np.loadtxt('ti11_2.txt'); m=a.shape[0]
b=zscore(a); z=sch.linkage(b)
sch.dendrogram(z, labels=np.arange(1,m+1))
plt.show()
n0=eval(input('请输入聚类的类数n0\n'))
cluster=sch.fcluster(z, t=n0, criterion='maxclust')
print('聚类的结果为：', cluster)



