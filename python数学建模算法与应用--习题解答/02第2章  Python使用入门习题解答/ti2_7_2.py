#程序文件ti2_7_2.py
import numpy as np

a=np.array([[2,3,1],[1,-2,4],[3,8,-2],[4,-1,9]])
b=np.array([[4],[-5],[13],[-6]])
r1=np.linalg.matrix_rank(a)
ab=np.hstack([a,b])
r2=np.linalg.matrix_rank(ab)
print("r1=",r1,", r2=",r2)
x=np.linalg.pinv(a)@b  #求最小范数解
print("最小范数解为：\n",np.round(x,4))
