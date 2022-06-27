#程序文件ti9_4.py
import numpy as np
import statsmodels.api as sm


y=np.loadtxt('ti9_4.txt').flatten()  #把表中的逗号替换为空格
x1=np.tile(np.arange(1,4),(12,1)).T.flatten()
x2=np.tile(np.hstack([np.ones(3),2*np.ones(3),3*np.ones(3),
                      4*np.ones(3)]),(3,1)).flatten()
d={'x1':x1, 'x2':x2, 'y':y}
md=sm.formula.ols('y~C(x1)*C(x2)',d).fit()
ano=sm.stats.anova_lm(md)
print(ano); print('总偏差平方和：', sum(ano.sum_sq))

