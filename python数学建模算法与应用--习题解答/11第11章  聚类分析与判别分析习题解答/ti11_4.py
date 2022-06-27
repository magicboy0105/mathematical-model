#程序文件ti11_4.py
import numpy as np
from scipy.stats import zscore
import scipy.cluster.hierarchy as sch
import pylab as plt

a=np.loadtxt('ti11_4.txt'); m=a.shape[0]
b=zscore(a); z=sch.linkage(b)
sch.dendrogram(z, labels=range(1,m+1))
plt.show()
n0=eval(input('请输入聚类的类数n0\n'))
cluster=sch.fcluster(z, t=n0, criterion='maxclust')
print('聚类的结果为：', cluster)

               





