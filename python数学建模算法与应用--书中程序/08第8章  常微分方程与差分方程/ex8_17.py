#程序文件ex8_17.py
import numpy as np
import pandas as pd

a = pd.read_excel('data8_13.xlsx', header=None)
b = a.values; xd = b[1::2,:]
xd = xd[~np.isnan(xd)]  #提出有效数据
A = np.vstack([xd[:-1], xd[:-1]**2]).T  #系数矩阵
cs = np.linalg.pinv(A) @ xd[1:]  #拟合参数
xh = cs[0]*xd[-1]+cs[1]*xd[-1]**2
print('参数值为：', np.round(cs,4))
print('2010年人口预测值为：', round(xh,4))








