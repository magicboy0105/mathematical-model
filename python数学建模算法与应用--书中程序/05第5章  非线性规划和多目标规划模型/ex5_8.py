#程序文件ex5_8.py
import numpy as np
from scipy.optimize import minimize

d = np.loadtxt('data5_8.txt')
a = d[0]; b = d[1]; c = d[2]
e = np.array([20, 20])

def obj(xyz):
    x = xyz[: 2]; y = xyz[2: 4]
    z = xyz [4:].reshape(6,2)
    obj =0
    for i in range(6):
        for j in range(2):
            obj = obj + z[i,j] * np.sqrt((x[j]-a[i])**2+(y[j]-b[i])**2)
    return obj

con = []
con.append({'type': 'eq', 'fun': lambda z: z[4:].reshape(6,2).sum(axis=1)-c})
con.append({'type': 'ineq', 'fun': lambda z: e-z[4:].reshape(6,2).sum(axis=0)})
bd = [(0, np.inf) for i in range(16)]  #决策向量的界限
res = minimize(obj, np.random.rand(16), constraints=con, bounds=bd)
print(res)  #输出解的信息
s=np.round(res.x, 4)     #提出最优解的取值
print('目标函数的最优值：', round(res.fun,4))
print('x的坐标为：', s[:2])
print('y的坐标为：', s[2:4])
print('料场到工地的运输量为：\n', s[4:].reshape(6,2).T)
