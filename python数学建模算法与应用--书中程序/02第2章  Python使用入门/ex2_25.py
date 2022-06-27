#程序文件ex2_25.py
import numpy as np
a1 = np.array([1, 2, 3, 4])   #生成整型数组
a2 = a1.astype(float)
a3 = np.array([1, 2, 3, 4], dtype=float)   #浮点数
print(a1.dtype); print(a2.dtype); print(a3.dtype)
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.arange(1,5)        #生成数组[1, 2, 3, 4]
d = np.linspace(1, 4, 4)  #生成数组[1, 2, 3, 4]
e = np.logspace(1, 3, 3, base=2)  #生成数组[2, 4, 8]
