#程序文件anli14_1_1
import numpy as np
from scipy.optimize import fsolve
import pylab as plt

f1 = lambda t: [1/(1+t[0]/(1-t[1])**2)-0.01,
                1/(1+t[0]/(3-t[1])**2)-0.8]
c1 = fsolve(f1, [0.5,0.5])    #待定参数alpha,beta
f2 = lambda t: [t[0]*np.log(3)+t[1]-0.8, t[0]*np.log(5)+t[1]-1]
c2 = fsolve(f2, [0.5, 0.5])   #待定参数a,b
fx = lambda x: (1/(1+c1[0]/(x-c1[1])**2) * ((x>=1)&(x<=3))+
               (c2[0]*np.log(x)+c2[1]) * ((x>3) & (x<=5)))
x0 = np.linspace(1, 5, 100); plt.plot(x0, fx(x0))
f2 =fx(2); f4 = fx(4)

d0 = np.loadtxt('anli14_1_1.txt')
d1 = d0[:,0]; d2 = d0[:,3:]
e20 = fx(d2); e21 = e20.mean(1) #逐行求均值得到综合复试成绩
e2 =  (e21-min(e21))/(max(e21)-min(e21))  #复试成绩标准化
e1 = (d1-min(d1))/(max(d1)-min(d1))  #初始成绩标准化
f = (e1 + e2) /2  #计算综合得分
ind = np.argsort(-f)  #从大到小排序的地址
ind[ind] = np.arange(1,len(ind)+1) #综合得分排序
print('综合得分：\n', f); print('综合得分排序：\n', ind)
np.savetxt('anli14_1_2.txt', f); plt.show()




                
