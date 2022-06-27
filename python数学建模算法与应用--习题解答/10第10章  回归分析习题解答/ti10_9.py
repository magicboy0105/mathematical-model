#程序文件ti10_9.py
import numpy as np
import pylab as plt
import statsmodels.api as sm

a=np.loadtxt('ti10_9.txt')
x=a[:,0]; y=a[:,3]
plt.rc('font',size=15)
plt.rc('font',family='SimHei')
plt.plot(x,y,'o'); plt.xlabel('年龄')
plt.ylabel('冠心病患病比例',rotation=90)

y1=a[:,2]  #患病（成功）人数
y2=a[:,1]-a[:,2]  #非患病（失败）人数
yy=np.vstack([y1,y2]).T
d={'yy':yy, 'x':x}
md=sm.formula.glm("yy~x", d,family=sm.families.Binomial()).fit()
print(md.summary()); cs=md.params  #提取拟合系数
px=lambda x: 1/(1+np.exp(-cs[0]-cs[1]*x)) #定义拟合的函数
x0=np.linspace(24,65,20)
plt.figure(); plt.plot(x,y,'o')
plt.plot(x0,px(x0)); plt.xlabel('年龄')
plt.ylabel('冠心病患病比例',rotation=90); plt.show()

