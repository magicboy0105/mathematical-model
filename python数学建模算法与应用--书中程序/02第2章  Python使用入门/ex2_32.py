#程序文件ex2_32.py
import numpy as np

a = np.ones(4)
b = np.arange(2, 10, 2)
c = a @ b  #a作为行向量,b作为列向量
d = np.arange(16).reshape(4,4)
f = a @ d  #a作为行向量
g = d @ a  #a作为列向量
