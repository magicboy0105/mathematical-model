#程序文件ti9_6_1.py
import numpy as np
from scipy.stats import norm, chi2, chisquare
import pylab as plt

n=100; k=8
a=np.loadtxt('ti9_6.txt').flatten()
plt.hist(a); plt.show()
mu=a.mean(); S=a.std(ddof=1)
print('均值：',mu); print('标准差：', S)
x1=a.min(); x2=a.max()  #求最小值和最大值
x=np.linspace(300, 900, k)  #逐步凑的分点
bin=np.hstack([x1, x, x2])    #统计频数的分点
h=plt.hist(a, bin); f=h[0]    #统计数据频数及提取频数值
p1=norm.cdf(x, mu, S)  #计算各个分点分布函数的取值
p2=np.hstack([p1[0], np.diff(p1), 1-p1[-1]])  #计算各区间概率
print('各区间的频数：', f)
print('各区间概率为：', np.round(p2,4))
ex=n*p2  #计算期望频数
kf1=chisquare(f, ex, ddof=2)   #调用库函数计算统计量的值
kf2=sum(f**2/(n*p2))-n         #直接计算统计量的值
ka=chi2.ppf(0.95, k-2)         #临界值
print(kf1); print(round(kf2,4))  #输出两种方法计算的统计量
