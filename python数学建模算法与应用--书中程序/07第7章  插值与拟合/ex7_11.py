#程序文件ex7_11.py
import numpy as np
import pylab as plt

a=np.loadtxt('data7_11.txt'); x=a[0]; y=a[1]
A=np.vstack([x**2,x*y,y**2,x,y]).T  #线性方程组系数矩阵
b=-np.ones(5)   #线性方程组的常数项
c=np.linalg.inv(A)@b  #解线性方程组拟合参数
print("拟合的系数为：\n",np.round(c,4))
f=lambda x,y: c[0]*x**2+c[1]*x*y+c[2]*y**2+c[3]*x+c[4]*y
x=np.linspace(3,8,100); y=np.linspace(-1,5,100)
x,y=np.meshgrid(x,y); z=f(x,y)
plt.rc('font',size=16); plt.rc('text',usetex=True)
plt.contour(x,y,z,[-1])   #画高度为-1的等高线
plt.xlabel('$x$'); plt.ylabel('$y$',rotation=0)
plt.show()

