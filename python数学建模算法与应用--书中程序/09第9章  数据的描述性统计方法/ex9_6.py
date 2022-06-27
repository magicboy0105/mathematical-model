#程序文件ex9_6.py
import numpy as np
import pandas as pd
df = pd.read_csv('data9_5.txt', header=None)
df = df.T  #转置
print(df.describe())
print('-----\n偏度：\n', df.skew())
print('-----\n峰度：\n', df.kurt())
print('-----\n90%分位数：\n', df.quantile(0.9))
