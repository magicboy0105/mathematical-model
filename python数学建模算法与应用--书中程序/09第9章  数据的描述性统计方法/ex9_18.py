#程序文件ex9_18.py
import pandas as pd
import numpy as np
import statsmodels.api as sm

a = pd.read_excel('data9_18.xlsx', header=None)
b = a.values.T; y = b[~np.isnan(b)]
x = np.hstack([np.ones(5), np.full(4,2), np.full(4,3), np.full(3,4)])
d = {'x':x, 'y':y}   #构造字典
model = sm.formula.ols('y~C(x)', d).fit()   #构建模型
anovat = sm.stats.anova_lm(model)  #进行单因素方差分析
print(anovat)

