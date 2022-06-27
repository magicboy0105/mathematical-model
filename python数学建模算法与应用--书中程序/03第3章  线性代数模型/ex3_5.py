#程序文件ex3_5.py
import numpy as np
from numpy.linalg import svd

a = np.array([[1, 0, 1], [0, 1, 1], [0, 0, 0]])
u,s,vt = svd(a);  a=u@np.diag(s)@vt
print(u); print(s); print(vt)
