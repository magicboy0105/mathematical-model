#程序文件ex7_5.py
from scipy.interpolate import UnivariateSpline, interp1d
import numpy as np

t0=np.linspace(0.15, 0.18, 4)
v0=np.array([3.5, 1.5, 2.5, 2.8])
sp1 = UnivariateSpline(t0, v0)  #求三次样条函数
print(sp1.get_coeffs())
print("第1种方法的积分值：",sp1.integral(0.15,0.18))  #求样条函数的积分
sp2=interp1d(t0,v0,'cubic')  #第二种方法
tn=np.linspace(0.15,0.18,200); vn=sp2(tn)
I2=np.trapz(vn,tn); print("第2种方法的积分值：", I2)




