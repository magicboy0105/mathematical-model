#程序文件ti5_5.py
from scipy.optimize import minimize
import numpy as np

obj=lambda x: -(2*x[0]+3*x[0]**2+3*x[1]+x[1]**2+x[2])
def constr(x):
    x1, x2, x3=x
    return [10-x1-2*x1**2-x2-2*x2**2-x3,
            50-x1-x1**2-x2-x2**2+x3,
            40-2*x1-x1**2-2*x2-x3, x1+2*x2-1]
con1={'type': 'ineq', 'fun': constr}  #不等号约束
con2={'type': 'eq', 'fun': lambda x: x[0]**2+x[2]-2} #等号约束
con = [con1, con2]  #构造全部约束条件
bd=[(0, None)]; bd2=list(zip([None]*2, [None]*2))
bd.extend(bd2)  #构造决策向量的下界和上界
res=minimize(obj,np.random.rand(3),constraints=con,bounds=bd)
print(res)

