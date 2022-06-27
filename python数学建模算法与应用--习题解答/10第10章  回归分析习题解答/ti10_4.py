#程序文件ti10_4.py
import numpy as np
import statsmodels.api as sm

a=np.loadtxt('ti10_4.txt')  
d={'y':a[:,0],'x1':a[:,1],'x2':a[:,2],'x3':a[:,3]}
md1=sm.formula.ols('y~x1+x2+x3', d).fit()
print(md1.summary())
md2=sm.formula.ols('y~x1+x2', d).fit()
print(md2.summary())
