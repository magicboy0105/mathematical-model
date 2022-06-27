#程序文件ti9_6_2.py
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

t=10; k=1000; f=200; d=3000
a=np.loadtxt('ti9_6.txt').flatten()
mu=a.mean(); S=a.std(ddof=1)
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
                          
        
        


