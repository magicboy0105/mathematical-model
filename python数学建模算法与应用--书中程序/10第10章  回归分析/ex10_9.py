#程序文件ex10_9.py
import numpy as np
import statsmodels.api as sm
from scipy.stats import norm

a = np.loadtxt("data10_7_1.txt")
x = a[:,0]; pi = a[:,2]/a[:,1]; yi = norm.ppf(pi)
X = sm.add_constant(x)
md = sm.OLS(yi, X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果
p0= norm.cdf(md.predict([1, 9]))
print("所求比例p0=%.4f"%p0)

