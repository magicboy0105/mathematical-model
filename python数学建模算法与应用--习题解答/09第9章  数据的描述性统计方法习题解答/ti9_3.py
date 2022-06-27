#程序文件ti9_3.py
import numpy as np
import pylab as plt
import pandas as pd
import statsmodels.api as sm
from scipy.stats import f

a = pd.read_excel('ti9_3.xlsx', header=None)
a.boxplot()  #画箱线图
b = a.values.flatten()
print('上alpha分位数为：', f.ppf(0.95, 6, 63))
x = np.tile(np.arange(1,8),(10,1)).flatten()
d = {'x' : x, 'y' : b}  #x为类别变量
model = sm.formula.ols('y~C(x)', d).fit()  
anova = sm.stats.anova_lm(model)  #进行单因素方差分析
print('总的偏差平方和：', round(sum(anova.sum_sq),4))
print(anova); plt.show()
