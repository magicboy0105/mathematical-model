#程序文件ex10_7_2.py
import numpy as np
import statsmodels.api as sm

a = np.loadtxt('data10_7_1.txt')
x = a[:,0]; y = np.vstack([a[:,2], a[:,1]-a[:,2]]).T
d = {'x':x, 'y':y}  #y的第1列为成功的次数，第2列为失败次数
md = sm.formula.glm('y~x',d, family=sm.families.Binomial()).fit()
print(md.summary())
