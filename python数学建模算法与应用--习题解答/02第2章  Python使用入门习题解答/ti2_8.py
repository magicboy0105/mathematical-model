#程序文件ti2_8.py
import numpy as np
from numpy.linalg import inv

a = 4*np.eye(1000)+np.eye(1000,k=-1)+np.eye(1000,k=1)
b = np.arange(1,1001).reshape(1000,1)
x = inv(a) @ b; print(x)
