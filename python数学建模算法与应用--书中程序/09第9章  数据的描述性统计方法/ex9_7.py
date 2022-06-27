#程序文件ex9_7.py
import pandas as pd
import pylab as plt

df = pd.read_csv('data9_5.txt', header=None)
df = df.T  #转置
plt.subplot(121); h1 = plt.hist(df[0], 5); print(h1)
plt.subplot(122); plt.hist(df[1], 5) 
df.hist(bins=5)   #另一种方法画直方图
plt.show()



