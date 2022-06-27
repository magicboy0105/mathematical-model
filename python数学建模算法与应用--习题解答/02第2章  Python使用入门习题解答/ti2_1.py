#程序文件ti2_1.py
import pylab as plt
import numpy as np

plt.rc('font',family='SimHei')  #用来正常显示中文标签
plt.rc('axes',unicode_minus=False)  #用来正常显示负号
x=np.linspace(-3,3,50)
y1=np.cosh(x); y2=np.sinh(x); y3=np.exp(x)/2
plt.plot(x,y1,'r-*',label="双曲余弦函数")
plt.plot(x,y2,'--.b',label="双曲正弦函数")
plt.plot(x,y3,'-.dk',label="指数函数")
plt.legend(); plt.show()
