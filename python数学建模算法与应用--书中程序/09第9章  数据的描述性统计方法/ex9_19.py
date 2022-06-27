#程序文件ex9_19.py
import numpy as np
import pandas as pd
from scipy.stats import f
import statsmodels.api as sm

d = np.loadtxt('data9_19.txt')
mu = d.mean(axis=1); a = d.flatten()
x=np.tile(np.arange(1,6), (4,1)).T.flatten()
d={'x':x,'y':a}  #构造求解需要的字典
m = sm.formula.ols("y~C(x)",d).fit()  #构建模型
s = sm.stats.anova_lm(m)  #进行单因素方差分析
fa = f.ppf(0.95, s.df[0], s.df[1])  #计算上alpha分位数
ts = sum(s.sum_sq)  #求总的偏差平方和
print(s); print('临界值：', round(fa,4))
print('总的偏差平方和：', round(ts,4))
