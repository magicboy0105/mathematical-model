#程序文件ex7_4.py
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange
import pylab as plt

a = np.loadtxt('data7_4.txt')
x0 = a[0]; y0 = a[1]
x = np.linspace(0,15,151)
yx1 = interp1d(x0, y0)  #分段线性插值
y1 = yx1(x)  #计算插值点的函数值
p2 = lagrange(x0, y0)  #计算Lagange插值
y2 = np.polyval(p2, x)
yx3 = interp1d(x0, y0, 'cubic')
y3 = yx3(x)
dx = np.diff(x); dy = np.diff(y3)
dyx = dy / dx; dyx0 = dyx[0]
xt = x[130:]; yt = y3[130:]
ymin = min(yt)
xmin = [xt[ind] for ind, v in enumerate(yt) if v==ymin]
print('x=0处斜率的数值解为：', dyx0)
print('xmin=', xmin); print('ymin=', ymin)
plt.rc('font', family='SimHei')      #用来正常显示中文标签
plt.rc('axes', unicode_minus=False)  #用来正常显示负号
plt.rc('font', size=16)
plt.subplots_adjust(wspace = 0.5)    #调整子图水平间距  
plt.subplot(131); plt.plot(x, y1)
plt.title('分段线性插值')
plt.subplot(132); plt.plot(x, y2)
plt.title('拉格朗日插值')
plt.subplot(133); plt.plot(x,y3)
plt.title('三次样条插值')
plt.show()


