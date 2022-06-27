#程序文件ti16_3.py
import numpy as np
from scipy.optimize import minimize

a = np.array([[2,5],[0,4]])
b = np.array([[2,0],[5,4]])
obj = lambda z: sum(z)  #定义虚拟的目标函数,z[0]=x1,z[1]=x2,z[2]=y1,z[3]=y2
con1 = {'type':'ineq','fun':lambda z:z[:2]@a@z[2:]-a@z[2:]}
con2 = {'type':'ineq','fun':lambda z:z[:2]@b@z[2:]-b.T@z[:2]}
con3 = {'type':'eq', 'fun':lambda z:sum(z[:2])-1}
con4 = {'type':'eq', 'fun':lambda z:sum(z[2:])-1}
con = [con1, con2, con3, con4]
bd = [(0, 1) for i in range(4)]
s = minimize(obj, 0.5*np.ones(4), constraints=con, bounds=bd)
print('解的详细信息如下：\n', s)
x = s.x[:2]; y = s.x[2:]
print('x的解为:',x); print('y的解为:',y)
print('国家I期望赢得:',x@a@y); print('国家II期望赢得:',x@b@y)

                             
