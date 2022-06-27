#程序文件 ex10_11.py
import numpy as np
import statsmodels.api as sm
a=np.loadtxt("data10_11.txt")
d = {'x1':a[:,0], 'x2':a[:,1], 'x3':a[:,2], 'y':a[:,-1]}
md = sm.formula.logit('y~x1+x2+x3', d)
md = md.fit(method='bfgs')  #使用默认牛顿方法出错
print(md.summary())
print(md.predict({'x1':[49.2,40.6],'x2':[-17.2,26.4],'x3':[0.3,1.8]}))  #求预测值
