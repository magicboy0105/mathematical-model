#程序文件ex9_5.py
import numpy as np
import pandas as pd
a = pd.read_csv('data9_5.txt', header=None)
b = a.values  #DataFrame转换为array数组
mu = np.mean(b, axis=1)   #求均值
zw = np.median(b, axis=1) #求中位数
jc = np.ptp(b, axis=1)    #求极差
fc = np.var(b, axis=1, ddof=1) #求方差
bz = np.std(b, axis=1, ddof=1) #求标准差
xf = np.cov(b)       #求协方差矩阵
xs = np.corrcoef(b)  #求相关系数矩阵
