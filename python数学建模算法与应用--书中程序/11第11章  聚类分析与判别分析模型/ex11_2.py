#程序文件ex11_2.py
import numpy as np
import scipy.cluster.hierarchy as sch
import pylab as plt

plt.rc('text', usetex=True); plt.rc('font', size=16)
a=np.loadtxt('data11_2.txt'); n=a.shape[0]
b=(a-a.min(axis=0))/(a.max(axis=0)-a.min(axis=0))
z=sch.linkage(b)
s=['$\\omega_'+str(i+1)+'$' for i in range(n)]
sch.dendrogram(z, labels=s); plt.show()


