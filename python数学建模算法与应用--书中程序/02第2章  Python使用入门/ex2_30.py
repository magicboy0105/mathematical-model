#程序文件ex2_30.py
import numpy as np
a = np.array([[0, 3, 4], [1, 6, 4]])
b = a.sum()   #使用方法，求矩阵所有元素的和
c1 = sum(a)   #使用内置函数，求矩阵逐列元素的和
c2 = np.sum(a, axis=0) #使用函数，求矩阵逐列元素的和
c3 = np.sum(a, axis=0, keepdims=True)   #逐列求和
print(c2.shape, c3.shape)  #c2是(3,)数组，c3是(1,3)数组
