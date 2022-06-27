#程序文件ti7_7.py
import numpy as np
from numpy.random import rand
from scipy.optimize import curve_fit, leastsq, least_squares

x0=np.arange(1,21)
gx=lambda x,a,b:10*a/(10*b+(a-10*b)*np.exp(-a*np.sin(x)))
y0=gx(x0,1.1,0.01)
pa1,cov1=curve_fit(gx,x0,y0,p0=rand(2))  #第1种拟合

def gh(p,x):   #定义拟合函数
    a,b=p
    return 10*a/(10*b+(a-10*b)*np.exp(-a*np.sin(x)))
err=lambda p,x,y: gh(p,x)-y  #定义误差向量匿名函数
pa2=leastsq(err,rand(2),args=(x0,y0))[0]    #第2种拟合
pa3=least_squares(err,rand(2),args=(x0,y0)) #第3种拟合
print("pa1=",pa1); print("pa2=",pa2)
print("--------------"); print("pa3=",pa3)
