#程序文件ex2_34.py
import numpy as np
a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x1 = np.linalg.inv(a) @ b  #第一种解法
#上面语句中@表示矩阵乘法
x2 = np.linalg.solve(a, b) #第二种解法
print(x1); print(x2)
