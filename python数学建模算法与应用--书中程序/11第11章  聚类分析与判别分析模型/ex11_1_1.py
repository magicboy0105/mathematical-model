#程序文件ex11_1_1.py
import scipy.cluster.hierarchy as sch
import numpy as np
import pylab as plt

plt.rc('text', usetex=True); plt.rc('font', size=16)
a=np.array([[2, 3, 3.5, 7, 9]]).T
c=sch.linkage(a)
s=['$\\omega_'+str(i+1)+'$' for i in range(5)]
sch.dendrogram(c, labels=s); plt.show()
