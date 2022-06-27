#程序文件ti10_5.py
import numpy as np
import statsmodels.api as sm

x=np.array([1,2,4,5,7,8,9,10])
y=np.array([1.3,1,0.9,0.81,0.7,0.6,0.55,0.4])
mat=np.stack([1/x,np.ones(8),x,x**2]).T
cs=np.linalg.pinv(mat)@y  #第1种方法拟合参数
print('拟合的参数为：',np.round(cs,4))
d={'y':y,'x':x}
md=sm.formula.ols('y~I(1/x)+x+I(x**2)',d).fit()
print(md.summary())  #输出第2种方法的求解结果
