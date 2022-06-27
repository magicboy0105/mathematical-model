#程序文件ti2_4.py
import pylab as plt
import numpy as np

plt.rc('text',usetex=True)
x=np.linspace(-10,10,50)
s=['*r-','ob-','sy-','pc-','Hg-','>k-']
fx=lambda x,k: k*x**2+2*k
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.plot(x,fx(x,i+1),s[i],label='$k$='+str(i+1))
    plt.legend()
plt.show()
