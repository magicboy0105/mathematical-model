#程序文件ex11_1_2.py
import scipy.cluster.hierarchy as sch
import pylab as plt

plt.rc('text', usetex=True); plt.rc('font', size=16)
a=[2, 3, 3.5, 7, 9]; n=len(a)
d = [abs(a[i]-a[j]) for i in range(n-1) for j in range(i+1,n)]
c=sch.linkage(d)
s=['$\\omega_'+str(i+1)+'$' for i in range(n)]
sch.dendrogram(c, labels=s); plt.show()

