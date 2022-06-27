#程序文件ex2_35.py
import numpy as np
a = np.array([[3, 1], [1, 2], [1, 1]])
b = np.array([9, 8, 6])
x = np.linalg.pinv(a) @ b  
print(np.round(x, 4))
