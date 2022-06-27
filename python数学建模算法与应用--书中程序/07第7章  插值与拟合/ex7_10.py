#程序文件ex7_10.py
import numpy as np
t=np.arange(8)
y=np.array([27.0, 26.8, 26.5, 26.3, 26.1, 25.7, 25.3, 24.8])
tb=t.mean(); yb=y.mean()
a1=sum((t-tb)*(y-yb))/sum((t-tb)**2)
b1=yb-a1*tb  
print('拟合的多项式系数：',[a1,b1])  #输出第一种方法的解
A=np.vstack([t, np.ones(len(t))]).T
p=np.linalg.pinv(A) @ y  
print('拟合的多项式系数：', p)   #输出第二种方法的解






