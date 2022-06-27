#程序文件ex9_10.py
import pandas as pd
import pylab as plt
from scipy.stats import norm, probplot

df = pd.read_csv('data9_5.txt', header=None)
d = df.values[0]  #提取甲班成绩
mu = d.mean(); s = d.std(); sd = sorted(d); n = len(d)
x = (plt.arange(n)+1/2)/n; yi = norm.ppf(x, mu, s)
plt.rc('font', size=16); plt.rc('font', family='SimHei')
plt.rc('axes', unicode_minus=False)
plt.subplot(121); plt.plot(yi, sd, 'o', label='QQ图')
plt.plot(sd, sd, label='参照直线'); plt.legend()
plt.subplot(122); probplot(d, plot=plt); plt.show()



