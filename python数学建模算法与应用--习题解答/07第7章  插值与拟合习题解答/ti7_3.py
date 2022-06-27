#程序文件ti7_3.py
import numpy as np
import pylab as plt
from scipy.interpolate import interp1d

T0=np.linspace(700, 780, 5)
V0=np.array([0.0977, 0.1218, 0.1406, 0.1551, 0.1664])
T=[750,770]
fv1=interp1d(T0,V0); fv2=interp1d(T0,V0,'cubic')
V1=fv1(T); V2=fv2(T)
xn=np.linspace(700,780,81)
vn1=fv1(xn); vn2=fv2(xn)
plt.rc('font',family='SimHei')
plt.plot(xn,vn1,'-*',label="线性插值")
plt.plot(xn,vn2,'.-',label="三次样条插值")
plt.legend(); plt.show()


