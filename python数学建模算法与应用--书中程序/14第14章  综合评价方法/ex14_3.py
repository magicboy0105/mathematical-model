#程序文件ex14_3.py
import numpy as np

a = np.array([[0.4,0.3,0.5,0.3],[0.3,0.3,0.4,0.4],[0.2,0.3,0.3,0.3]])
b = np.array([0.2,0.3,0.4,0.3]); n = a.shape[0]; N=[]
for e in a: N.append(1-sum(abs(e-b))/3)
print("贴近度为：",np.round(N,4))
