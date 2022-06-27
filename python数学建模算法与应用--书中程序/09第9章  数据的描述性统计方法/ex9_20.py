#程序文件ex9_20.py
import numpy as np
from scipy.stats import f
import statsmodels.api as sm

a = np.loadtxt('data9_20.txt')
x1 = np.tile(np.arange(1,5), (3,1)).T    #燃料水平
x2 = np.tile(np.arange(1,4), (4,1))      #推进器水平
d = {'x1':x1.flatten(), 'x2':x2.flatten(), 'y':a.flatten()}
m = sm.formula.ols('y~C(x1)+C(x2)', d).fit()
s = sm.stats.anova_lm(m); print(s)

