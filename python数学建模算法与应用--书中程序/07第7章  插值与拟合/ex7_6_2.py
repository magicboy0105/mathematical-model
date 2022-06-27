#程序文件ex7_6_2.py
import numpy as np
import pylab as plt

a=np.loadtxt('data7_6.txt')
x0=a[::3].flatten()  #提出点的横坐标
y1=a[1::3].flatten()  #提出下边界的纵坐标
y2=a[2::3].flatten()  #提出上边界的纵坐标
L=np.trapz(np.sqrt(1+np.gradient(y1,x0)**2)+
           np.sqrt(1+np.gradient(y2,x0)**2),x0)
L=L/18*40; print('周长L=',round(L,4))
S=np.trapz(y2-y1,x0); S=S/18**2*1600
print('面积S=',round(S,4)); delta=(S-41288)/41288
print('相对误差delta=',round(delta,4))





