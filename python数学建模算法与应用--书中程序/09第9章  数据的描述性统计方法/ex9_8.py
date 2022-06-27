#程序文件ex9_8.py
import pandas as pd
import pylab as plt

df = pd.read_csv('data9_5.txt', header=None).T
plt.rc('font', family='SimHei'); plt.rc('font', size=16);
plt.boxplot(df, labels=['甲班', '乙班']); plt.show()
