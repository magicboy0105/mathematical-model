#程序文件ex5_5.py
import numpy as np
from scipy.optimize import minimize

c2 = np.array([[-1, -0.15],[-0.15, -2]])
c1 = np.array([98, 277])
a = np.array([[1, 1], [1, -2]])
b = np.array([100, 0])
obj = lambda x: x @ c2 @ x + c1 @ x
con ={'type': 'ineq', 'fun': lambda x: b-a@x}
bd = [(0, np.inf) for i in range(a.shape[1])]
res = minimize(obj, np.random.randn(2), constraints=con, bounds=bd)
print(res)  #输出解的信息
