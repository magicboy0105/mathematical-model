#程序文件ex5_6.py
import numpy as np
from scipy.optimize import minimize

obj=lambda x: sum(x**2)+8
def constr1(x):
    x1, x2, x3 = x
    return [x1**2-x2+x3**2,
            20-x1-x2**2-x3**2]
def constr2(x):
    x1, x2, x3 = x
    return [-x1-x2**2+2, x2+2*x3**2-3]
con1={'type': 'ineq', 'fun': constr1}
con2={'type': 'eq', 'fun': constr2}            
con=[con1, con2]  #构造全部约束条件
bd = [(0, np.inf) for i in range(3)]
res = minimize(obj, np.random.randn(3), constraints=con, bounds=bd)
print(res)  #输出解的信息
