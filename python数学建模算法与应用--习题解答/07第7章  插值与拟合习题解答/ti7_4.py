#程序文件ti7_4.py
import numpy as np
import pylab as plt
import numpy.random as nr
from scipy.interpolate import griddata

z=lambda x,y: (x**2-2*x)*np.exp(-x**2-y**2-x*y)  #定义匿名函数
x0=nr.uniform(-3, 3, 60); y0=nr.uniform(-4, 4, 60)
z0=z(x0, y0)                #计算散乱点对应的函数值
xn=np.linspace(-3, 3, 61)   #插值节点的x坐标
yn=np.linspace(-4, 4, 81)   #插值节点的y坐标
xn, yn=np.meshgrid(xn, yn)  #生成网格节点数据
xy0=np.vstack([x0,y0]).T
zn1=griddata(xy0, z0, (xn, yn), method='cubic')   #三次样条插值
zn2=griddata(xy0, z0, (xn, yn), method='nearest')  #最近邻插值
zn1[np.isnan(zn1)]=zn2[np.isnan(zn1)]  #把nan值替换掉
ax1=plt.subplot(121,projection='3d')
ax1.plot_surface(xn, yn, z(xn,yn), cmap='summer')
ax2=plt.subplot(122,projection='3d')
ax2.plot_surface(xn, yn, zn1, cmap='winter'); plt.show()
