#程序文件ex8_13.py
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

a = pd.read_excel('data8_13.xlsx', header=None)
b = a.values; xd = b[1::2,:]
xd = xd[~np.isnan(xd)]  #提出有效数据
td = np.linspace(1790,2000,22)
x=lambda t, r, xm: xm/(1+(xm/3.9-1)*np.exp(-r*(t-1790)))
bd=[(0, 200), (0.1,1000)]  #约束两个参数的下界和上界
p1 =curve_fit(x, td[1:], xd[1:], bounds=bd)[0] #拟合参数
print(p1); print("2010年的预测值为：", round(x(2010,*p1),4))

n = len(xd)
b1 = np.diff(xd)/10/xd[:-1]  #构造常数项列
a1 = np.vstack([np.ones(n-1), -xd[:-1]]).T
p2 = np.linalg.pinv(a1) @ b1
r = p2[0]; xm = r/p2[1]; xh2 = x(2010, r, xm)
print('----------'); print(round(r,4))
print(round(xm,4)); print(round(xh2,4))

b2 = np.diff(xd)/10/xd[1:]  #构造常数项列
a2 = np.vstack([np.ones(n-1), -xd[1:]]).T
p3 = np.linalg.pinv(a2) @ b2
r = p3[0]; xm = r/p3[1]; xh3 = x(2010, r, xm)
print('----------'); print(round(r,4))
print(round(xm,4)); print(round(xh3,4))
