#程序文件ex7_7.py
import pylab as plt
import numpy as np
from numpy.linalg import norm
from scipy.interpolate import interp2d

z=np.loadtxt("data7_7.txt")  #加载高程数据
x=np.arange(0,1500,100)
y=np.arange(1200,-100,-100)
f=interp2d(x, y, z)  #双线性插值
xn=np.linspace(0,1400,141)
yn=np.linspace(0,1200,121)
zn=f(xn, yn)  #计算插值点的函数值
m=len(xn); n=len(yn); s=0; 
for i in np.arange(m-1):
    for j in np.arange(n-1):
        p1=np.array([xn[i],yn[j],zn[j,i]])
        p2=np.array([xn[i+1],yn[j],zn[j,i+1]])
        p3=np.array([xn[i+1],yn[j+1],zn[j+1,i+1]])
        p4=np.array([xn[i],yn[j+1],zn[j+1,i]])
        p12=norm(p1-p2); p23=norm(p3-p2); p13=norm(p3-p1)
        p14=norm(p4-p1); p34=norm(p4-p3);
        L1=(p12+p23+p13)/2
        s1=np.sqrt(L1*(L1-p12)*(L1-p23)*(L1-p13))
        L2=(p13+p14+p34)/2
        s2=np.sqrt(L2*(L2-p13)*(L2-p14)*(L2-p34))
        s=s+s1+s2;   
print("区域的面积为：", s)
plt.rc('font',size=16); plt.rc('text',usetex=True)
plt.subplot(121); contr=plt.contour(xn,yn,zn);
plt.clabel(contr); plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
ax=plt.subplot(122,projection='3d'); 
X,Y=np.meshgrid(xn,yn)
ax.plot_surface(X, Y, zn, cmap='viridis')
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$z$'); plt.show()





