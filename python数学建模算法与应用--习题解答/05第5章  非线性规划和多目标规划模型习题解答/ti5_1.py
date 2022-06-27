#程序文件ti5_1.py
from scipy.optimize import minimize
import numpy as np
a=np.array([[1,4,5],[4,2,6],[5,6,3]])
obj=lambda x:x@a@x
con={'type':'eq','fun':lambda x:x@x-1}
res=minimize(obj, np.random.randn(3), constraints=con)
print(res)
