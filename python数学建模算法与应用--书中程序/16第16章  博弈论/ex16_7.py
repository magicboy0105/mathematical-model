#程序文件ex16_7.py
import numpy as np
from scipy.optimize import minimize

a = np.array([[14,13,12],[13,12,12],[12,12,13]])
b = np.array([[13,14,15],[14,15,15],[15,15,14]])
obj = lambda z: sum(z)  #定义虚拟的目标函数
con1 = {'type':'ineq','fun':lambda z:z[:3]@a@z[3:]-a@z[3:]}
con2 = {'type':'ineq','fun':lambda z:z[:3]@b@z[3:]-b.T@z[:3]}
con3 = {'type':'eq', 'fun':lambda z:sum(z[:3])-1}
con4 = {'type':'eq', 'fun':lambda z:sum(z[3:])-1}
con = [con1, con2, con3, con4]
bd = [(0, 1) for i in range(6)]
s = minimize(obj, np.ones(6), constraints=con, bounds=bd)
print('解的详细信息如下：\n', s)
x = s.x[:3]; y = s.x[3:]
print('x的解为:',x); print('y的解为:',y)
print('甲队平均得分:',x@a@y); print('乙队平均得分:',x@b@y)

                             
