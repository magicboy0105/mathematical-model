#程序文件ti2_7_1.py
import numpy as np

a=np.array([[4,2,-1],[3,-1,2],[11,3,0]])
b=np.array([[2],[10],[8]])
r1=np.linalg.matrix_rank(a)
ab=np.hstack([a,b])
r2=np.linalg.matrix_rank(ab)
print("r1=",r1,", r2=",r2)
x=np.linalg.pinv(a)@b  #求最小二乘解
print("最小二乘解为：\n",np.round(x,4))
