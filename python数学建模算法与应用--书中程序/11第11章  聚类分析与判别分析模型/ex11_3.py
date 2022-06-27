#程序文件ex11_3.py
import numpy as np
import scipy.cluster.hierarchy as sch
import pylab as plt

plt.rc('text',usetex=True)
a=np.array([[2, 3, 3.5, 7, 9]]).T; n=len(a)
c=sch.linkage(a, 'complete', 'mahalanobis')
s=['$\\omega_'+str(i+1)+'$' for i in range(n)]
sch.dendrogram(c, labels=s); plt.show()
n0=eval(input('请输入聚类的类数n0:\n'))
cluster= sch.fcluster(c, t=n0, criterion='maxclust')
print('聚类的结果为：',cluster)
