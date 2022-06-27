#程序文件名ex7_19.py
import numpy as np
from scipy.interpolate import interp1d
import pylab as plt

a = np.loadtxt('data7_19.txt')
liu=a[::2,:].flatten()   #提出水流量并按照顺序变成行向量
sha=a[1::2,:].flatten()  #提出含沙量并按照顺序变成行向量
y = sha * liu   #计算排沙量
i = np.arange(1, 25); t = (12*i-4)*3600
t1=t[0]; t2=t[-1]
f = interp1d(t, y, 'cubic')  #进行三次样条插值
tt = np.linspace(t1, t2, 10000)  #取的插值节点
TL = np.trapz(f(tt), tt)   #求总含沙量的数值积分
print('总含沙量为：', TL)

plt.rc('font', family='SimHei'); plt.rc('font', size=16)
plt.subplot(121); plt.plot(liu[:11], y[:11],'*')
plt.xlabel('第一阶段')
plt.subplot(122); plt.plot(liu[11:], y[11:],'*')
plt.xlabel('第二阶段') 

rmse1 = np.zeros(2)  #第一阶段剩余标准差初始化
rmse2 = np.zeros(2)  #第二阶段剩余标准差初始化
for i in range(1,3):
    nh1 = np.polyfit(liu[:11], y[:11], i)  #拟合多项式
    print('第一阶段，', i, '次多项式系数:', nh1)
    yh1 = np.polyval(nh1, liu[:11])  #求预测值
    cha1 = sum((y[:11]-yh1)**2)  #求误差平方和
    rmse1[i-1] = np.sqrt(cha1/(10-i))
print('剩余标准差分别为：', rmse1)
for i in range(1,3):
    nh2 = np.polyfit(liu[11:], y[11:], i)  #拟合多项式
    print('第二阶段，', i, '次多项式系数:', nh2)
    yh2 = np.polyval(nh2, liu[11:])  #求预测值
    cha2 = sum((y[11:]-yh2)**2)  #求误差平方和
    rmse2[i-1] = np.sqrt(cha2/(12-i))
print('剩余标准差分别为：', rmse2)
plt.show()


