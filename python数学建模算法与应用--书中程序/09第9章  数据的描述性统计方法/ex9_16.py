#程序文件ex9_16.py
import scipy.stats as ss
import numpy as np

t = np.array([100, 200, 300, np.inf])
p0 = ss.expon.cdf(t, scale=200)    #计算分布函数的取值
p = np.hstack([p0[0], np.diff(p0)])  #计算区间上的概率
ob = np.array([121, 78, 43, 58])
n = sum(ob); ex = n * p
kf, p = ss.chisquare(ob, ex)  #输出统计量和概率值
yz = ss.chi2.ppf(0.95, 3)  #临界值
print('检验统计量的值：', round(kf,4))  #输出统计量值
