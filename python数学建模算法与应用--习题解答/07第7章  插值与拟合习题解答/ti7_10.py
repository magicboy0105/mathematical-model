#程序文件ti7_10.py
import numpy as np
from scipy.interpolate import interp1d, lagrange
import pylab as plt
from scipy.optimize import curve_fit

a = np.loadtxt('ti7_10.txt')
x0 = a[::2].flatten()   #提出x的观测值数据
y0 = a[1::2].flatten()  #提出y的观测值数据
p1 = lagrange(x0,y0)   #Lagrange插值
yx1 = interp1d(x0,y0)  #分段线性插值
yx2 = interp1d(x0,y0,'quadratic')
yx3 = interp1d(x0,y0,'cubic')
x = np.linspace(-2,4.9,200)
plt.rc('font', family='SimHei')
plt.rc('axes', unicode_minus=False)
plt.subplot(221); plt.plot(x,np.polyval(p1,x))
plt.title('Lagrange插值')
plt.subplot(222); plt.plot(x, yx1(x))
plt.title('分段线性插值')
plt.subplot(223); plt.plot(x, yx2(x))
plt.title('二次样条插值')
plt.subplot(224); plt.plot(x, yx3(x))
plt.title('三次样条插值')

m=len(x0)  #观测值的个数
RMSE = []; S = []  #剩余标准差和系数结果初始化
for n in range(1,5):
    p = np.polyfit(x0, y0, n)
    rmse = np.sqrt(sum((np.polyval(p,x0)-y0)**2)/(m-n-1))
    RMSE.append(rmse); S.append(p)
ind = np.argmin(RMSE) #求RMSE最小值的地址
print('拟合的多项式次数：',ind+1)
print(np.round(S[ind],4))    
    
yx = lambda x,m,s: 1/(np.sqrt(2*np.pi)*s)*np.exp(-(x-m)**2/(2*s**2))
cs = curve_fit(yx, x0, y0)[0]
print('拟合的系数：', np.round(cs,4))
yh = yx(x, *cs)  #计算拟合函数的取值
plt.figure(); plt.plot(x, yh) #画拟合函数的曲线
plt.show()
