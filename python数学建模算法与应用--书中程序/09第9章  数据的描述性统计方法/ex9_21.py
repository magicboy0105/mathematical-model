#程序文件ex9_21.py
import numpy as np
from scipy.stats import f
import statsmodels.api as sm

a = np.loadtxt('data9_21.txt')
x1 = np.tile(np.arange(1,5), (6,1)).T
x2 = np.tile(np.array([1,1,2,2,3,3]), (4,1))
d = {'x1':x1.flatten(), 'x2':x2.flatten(), 'y':a.flatten()}
m = sm.formula.ols('y~C(x1)*C(x2)', d).fit()
s = sm.stats.anova_lm(m); print(s)

