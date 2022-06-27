#程序文件ex12_4.py
import numpy as np

r=np.array([[1, 1/5, -1/5],[1/5, 1, -2/5],[-1/5, -2/5, 1]])
val,vec=np.linalg.eig(r)  #求相关系数阵的特征值和特征向量
A0=vec*np.sqrt(val)       #利用矩阵广播求载荷矩阵
print('特征值:',val,'\n载荷矩阵：\n',A0,'\n----------')
num=int(input("请输入选择公共因子的个数："))
A=A0[:,:num]              #提出num个因子的载荷矩阵
Ac=np.sum(A**2, axis=0)   #逐列元素求和，求信息贡献
Ar=np.sum(A**2, axis=1)   #逐行元素求和，求共同度
print("对x的贡献为：",Ac)
print("共同度为：",Ar)

