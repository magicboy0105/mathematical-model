#程序文件ti9_6.py
import numpy as np
from scipy.stats import norm, chi2, chisquare
import pylab as plt
from scipy.integrate import quad

N=100; K=8
a=np.loadtxt('ti9_6.txt').flatten()
plt.hist(a); plt.show()
mu=a.mean(); S=a.std(ddof=1)
print('均值：',mu); print('标准差：', S)
x1=a.min(); x2=a.max()  #求最小值和最大值
x=np.linspace(300, 900, K)  #逐步凑的分点
bin=np.hstack([x1, x, x2])    #统计频数的分点
h=plt.hist(a, bin); f=h[0]    #统计数据频数及提取频数值
p1=norm.cdf(x, mu, S)  #计算各个分点分布函数的取值
p2=np.hstack([p1[0], np.diff(p1), 1-p1[-1]])  #计算各区间概率
print('各区间的频数：', f)
print('各区间概率为：', np.round(p2,4))
ex=N*p2  #计算期望频数
kf1=chisquare(f, ex, ddof=2)   #调用库函数计算统计量的值
kf2=sum(f**2/(N*p2))-N         #直接计算统计量的值
ka=chi2.ppf(0.95, K-2)         #临界值
print(kf1); print(round(kf2,4))  #输出两种方法计算的统计量
print('-----------------------')

t=10; k=1000; f=200; d=3000
G=lambda x: norm.cdf(x, mu, S)  #定义分布函数
n=np.arange(15,41); s=np.arange(10,31); TEL=[]
for i in n:
    for j in s:
        m=i*j; I=quad(G,0,m-i)[0]
        EC=(((j-1)*t+k)*(1-G(m))+t/i*(m-i)*G(m-i)+
            (d+(i+1)*f/2)*(G(m-i)-G(0))-t/i*I)
        ER=m-m*G(m)+(m-i)*G(m-i)-I
        TEL.append([i, m, EC/ER])
TEL=np.array(TEL); ind=np.argmin(TEL[:,2])  #求最小值的地址
n0=TEL[ind,0]; m0=TEL[ind,1]
print('检查间隔：', n0); print('更换周期：', m0)
print('最小费用为：', TEL[ind,2])
