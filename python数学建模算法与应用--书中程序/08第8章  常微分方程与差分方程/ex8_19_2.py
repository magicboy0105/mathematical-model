#程序文件ex8_19_2.py
import numpy as np
import pylab as plt
from scipy.optimize import minimize

a = 1 - 0.2**(1/12); m = 1.109 * 10 ** 5
w = [5.07, 11.55, 17.86, 22.99]
#决策向量z的排序为x1,x2,x3,x4,k
n = lambda z: m/2*(1-a-0.42*z[4])**8*z[2]+m*(1-a-z[4])**8*z[3]
b = lambda z: 1.22*10**11/(1.22*10**11+n(z)) 
obj = lambda z: -(0.42*z[4]*w[2]*(1-(1-a-0.42*z[4])**8)/(a+0.42*z[4])*z[2]+
                  z[4]*w[3]*(1-(1-a-z[4])**8)/(a+z[4])*z[3])
con = [{'type': 'eq', 'fun': lambda z: z[0]-b(z)*n(z)},
       {'type': 'eq', 'fun': lambda z: z[1]-(1-a)**12*z[0]},
       {'type': 'eq', 'fun': lambda z: z[2]-(1-a)**12*z[1]},
       {'type': 'eq', 'fun': lambda z: z[3]-(1-a-0.42*z[4])**8*(1-a)**4*z[2]}]
bd = [(10**9, np.inf) for i in range(4)]  #决策向量的界限
bd.append((0, 1-a))
res = minimize(obj, 1000*np.random.rand(5), constraints=con, bounds=bd)
print(res)  #输出解的信息
print('最优解：', np.round(res.x, 4))
print('目标函数的最优值：', round(res.fun,4))




                        
    






