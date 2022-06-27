#程序文件ex10_7_1.py
import numpy as np
import statsmodels.api as sm

a = np.loadtxt('data10_7_1.txt')
x = a[:,0]; pi = a[:,2]/a[:,1]
X = sm.add_constant(x); yi=np.log(pi/(1-pi))
md = sm.OLS(yi, X).fit()  #构建并拟合模型
print(md.summary())  #输出模型的所有结果
p0=1/(1+np.exp(-md.predict([1,9])))
b = md.params  #提出回归系数
print("所求比例p0=%.4f"%p0)
np.savetxt("data10_7_2.txt", b) 
