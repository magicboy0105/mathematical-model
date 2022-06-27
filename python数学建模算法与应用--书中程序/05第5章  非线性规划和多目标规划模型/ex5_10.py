#程序文件ex5_10.py
import numpy as np
import pandas as pd
from scipy.optimize import minimize

x0=np.array([150, 85, 150, 145, 130, 0])
y0=np.array([140, 85, 155, 50, 150, 0])
q=np.array([243, 236, 220.5, 159, 230, 52])
d=np.zeros((6,6)); a0=np.zeros((6,6)); b0=np.zeros((6,6))
xy0=np.vstack([x0,y0]).T
for i in range(6):
    for j in range(6): d[i,j]=np.linalg.norm(xy0[i]-xy0[j])
d[d==0]=np.inf
a0=np.arcsin(8.0/d)*180/np.pi
xy1=x0+1j*y0; xy2=np.exp(1j*q*np.pi/180)
for m in range(6):
    for n in range(6):
        if n!=m: b0[m,n]=np.angle((xy2[n]-xy2[m])/(xy1[m]-xy1[n]))
b0=b0*180/np.pi
f=pd.ExcelWriter('data5_10.xlsx')  #创建文件对象
pd.DataFrame(a0).to_excel(f,"sheet1",index=None)  #把a0写入Excel文件
pd.DataFrame(b0).to_excel(f,"sheet2",index=None)  #把b0写入表单2
f.save()
obj=lambda x: sum(np.abs(x))
bd=[(-30,30) for i in range(6)]   #决策向量的界限
x0 = 30*np.random.rand(6)  #决策变量的初值
cons=[]
for i in range(5):
    for j in range(i+1,6):
        cons.append({'type': 'ineq', 'fun': lambda x:
                     np.abs(b0[i,j]+(x[i]+x[j])/2)-a0[i,j]})
res = minimize(obj, x0, constraints=cons, bounds=bd)
print(res); print('---------------')
print('目标函数的最优值：', round(res.fun, 4))
print('最优解为：', np.round(res.x, 4))
