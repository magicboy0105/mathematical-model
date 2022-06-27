#程序文件ex10_8_2.py
import numpy as np
import statsmodels.api as sm

a = np.loadtxt('data10_8.txt')
x = np.vstack([a[:, 1:4], a[:, 6:-1]])
y = np.hstack([a[:, 4], a[:, 9]])
d={'x1': x[:,0], 'x2':x[:,1], 'x3':x[:,2], 'y':y}
md1 = sm.formula.glm('y~x1+x2+x3', d, family=sm.families.Binomial()).fit()
print(md1.summary())
md2 = sm.formula.glm('y~x1+x3', d, family=sm.families.Binomial()).fit()
print(md2.summary())
