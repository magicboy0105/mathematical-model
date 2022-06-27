#程序文件名ex7_16.py
import numpy as np
from scipy.optimize import curve_fit, least_squares, leastsq
import pylab as plt

np.random.seed(1)  #进行一致性比较
m=200; n=300
x=np.linspace(-6, 6, m); y=np.linspace(-8, 8, n);
x2, y2 = np.meshgrid(x, y)
x3=x2.flatten(); y3=y2.flatten()
xy=np.vstack([x3,y3])
zxy = lambda t,m1,m2,s: np.exp(-((t[0]-m1)**2+(t[1]-m2)**2)/(2*s**2))
z=zxy(xy, 1, 4, 6)  #无噪声函数值
zr=z+0.2*np.random.normal(size=z.shape) #噪声数据
p1=curve_fit(zxy, xy, zr)[0]   #拟合参数
print("三个参数的拟合值分别为：", p1)
zn=zxy(xy, *p1)  #计算拟合函数的值
zn2=np.reshape(zn, x2.shape)
plt.rc('font',size=16)
ax=plt.axes(projection='3d')  #创建一个三维坐标轴对象
ax.plot_surface(x2, y2, zn2,cmap='gist_rainbow')

p0 = np.random.randn(3)  #拟合参数的初值
fun = lambda t, x, y: np.exp(-((x-t[0])**2 +(y-t[1])**2)/(2*t[2]**2))
err = lambda t, x, y, z: fun(t,x,y)- z  #定义误差向量
p2 = least_squares(err, p0, args=(x3,y3,zr))
print('p2:', p2)
p3 = leastsq(err, p0, args=(x3,y3,zr))
print('p3:', p3)
plt.savefig("figure7_15.png", dpi=500); plt.show()
