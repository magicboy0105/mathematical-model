#程序文件ti7_2.py
import numpy as np
import pandas as pd
from scipy.interpolate import interp2d
from numpy.linalg import norm
import pylab as plt

a=pd.read_excel('附件1：区域高程数据.xlsx',header=None,nrows=874)
b=a.values; [m,n]=b.shape
x0=np.arange(m)*50; y0=np.arange(n)*50
f=interp2d(x0,y0,b.T,'cubic')
xn=np.arange(0,(m-1)*50+1,25)  #插值节点的x坐标
yn=np.arange(0,(n-1)*50+1,25)  #插值节点的y坐标
zn=f(xn,yn); zn=zn.T; S=0
for i in np.arange(len(xn)-1):
    for j in np.arange(len(yn)-1):
        p1=np.array([xn[i],yn[j],zn[i,j]])
        p2=np.array([xn[i+1],yn[j],zn[i+1,j]])
        p3=np.array([xn[i+1],yn[j+1],zn[i+1,j+1]])
        p4=np.array([xn[i],yn[j+1],zn[i,j+1]])
        p12=norm(p1-p2); p23=norm(p3-p2); p13=norm(p3-p1);
        p14=norm(p4-p1); p34=norm(p4-p3);
        L1=(p12+p23+p13)/2;s1=np.sqrt(L1*(L1-p12)*(L1-p23)*(L1-p13));
        L2=(p13+p14+p34)/2; s2=np.sqrt(L2*(L2-p13)*(L2-p14)*(L2-p34));
        S=S+s1+s2;   
print("区域的面积为：", S)

