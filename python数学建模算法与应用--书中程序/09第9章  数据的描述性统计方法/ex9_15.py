#程序文件ex9_15.py
import scipy.stats as ss
import numpy as np

n1 =np.array([36, 40, 19, 2, 0, 2, 1])
f = np.arange(7)
lamda = n1@f/100; n = sum(n1)
p0 = ss.poisson.pmf(range(3), lamda)  #计算取值的概率
p = np.hstack([p0, 1-sum(p0)])   #构造分布律
ex = n * p; ob = np.hstack([n1[:3], sum(n1[3:])])  #计算期望频数和观测频数
kf1 = ss.chisquare(ob, ex, ddof=1).statistic
kf2 = sum(ob **2 / (n * p)) - n  #计算统计量的值
yz = ss.chi2.ppf(0.95, 2)  #临界值
print(kf1); print(kf2)  #输出两种方法计算的统计量

