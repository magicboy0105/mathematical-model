#程序文件ti9_5.py
import numpy as np
import statsmodels.api as sm

y=np.loadtxt('ti9_5.txt').T.flatten()  
x1=np.tile(np.hstack([np.ones(4),2*np.ones(4),3*np.ones(4)]),
           (4,1)).flatten()
x2=np.tile(np.tile([1,1,2,2],(1,3)),(4,1)).flatten()
x3=np.tile(np.tile([1,2],(1,6)),(4,1)).flatten()
d={'x1':x1, 'x2':x2, 'x3':x3, 'y':y}
md=sm.formula.ols('y~C(x1)*C(x2)*C(x3)',d).fit()
ano=sm.stats.anova_lm(md)
print(ano); print('总偏差平方和：', sum(ano.sum_sq))

