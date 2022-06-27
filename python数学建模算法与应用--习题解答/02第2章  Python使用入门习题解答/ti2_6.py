#程序文件ti2_6.py
import numpy as np
import pandas as pd
from numpy.linalg import norm
import pylab as plt

a=pd.read_excel('附件1：区域高程数据.xlsx',header=None,nrows=874)
b=a.values; [m,n]=b.shape
x0=np.arange(m)*50; y0=np.arange(n)*50; s = 0
for i in np.arange(m-1):
    for j in np.arange(n-1):
        p1=np.array([x0[i],y0[j],b[i,j]])
        p2=np.array([x0[i+1],y0[j],b[i+1,j]])
        p3=np.array([x0[i+1],y0[j+1],b[i+1,j+1]])
        p4=np.array([x0[i],y0[j+1],b[i,j+1]])
        p12=norm(p1-p2); p23=norm(p3-p2); p13=norm(p3-p1);
        p14=norm(p4-p1); p34=norm(p4-p3);
        L1=(p12+p23+p13)/2;s1=np.sqrt(L1*(L1-p12)*(L1-p23)*(L1-p13));
        L2=(p13+p14+p34)/2; s2=np.sqrt(L2*(L2-p13)*(L2-p14)*(L2-p34));
        s = s+s1+s2;   
print("区域的面积为：", s)
plt.rc('font',size=16); plt.rc('text',usetex=True)
ax=plt.subplot(121,projection='3d'); 
X,Y=np.meshgrid(x0,y0)
ax.plot_surface(X, Y, b.T,cmap='viridis')
ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
plt.subplot(122); plt.contour(x0,y0,b.T,50); plt.colorbar()
plt.plot(30000,0,'pr') #画出A点位置
plt.text(30500,200,'A') #标注A点
plt.plot(43000,30000,'pr') #画出B点位置
plt.text(43500,29500, 'B') #标注B点
plt.xlabel('$x$'); plt.ylabel('$y$',rotation=90)
plt.savefig('figure2_6.png',dpi=500); plt.show()
