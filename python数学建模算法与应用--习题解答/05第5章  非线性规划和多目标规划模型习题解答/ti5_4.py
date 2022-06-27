#程序文件ti5_4.py
import numpy as np
from scipy.optimize import minimize
obj=lambda x:-sum(np.sqrt(x))
a=np.zeros((5,100))
for i in range(4):
    for j in range(i+1):
        a[i,j]=j+1
a[4,:]=101-np.arange(1,101)
b=np.hstack([np.arange(10,49,10),1000])
cons={'type':'ineq','fun':lambda x:b-a@x}
bd=tuple(zip([0]*100,[1000]*100))      
res=minimize(obj,np.random.rand(100),constraints=cons,bounds=bd)
print(res)

