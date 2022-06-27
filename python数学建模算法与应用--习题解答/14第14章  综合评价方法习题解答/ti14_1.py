#程序文件ti14_1.py
import numpy as np

a = np.loadtxt('ti14_1.txt').T; m,n = a.shape
m1 = a.max(axis=0); m2 = a.min(axis=0)  #逐列求最大值和最小值
b = (a-m2)/(m1-m2)  #所有指标值都按效益型标准化
for j in np.array([1,5,7,9])-1:  #成本型指标值额外处理
    b[:, j] = (m1[j]-a[:,j])/(m1[j]-m2[j])
cp = b.max(axis=0); cm = b.min(axis=0)  #求正理想解和负理想解
d1 = np.linalg.norm(b-cp, axis=1)  #求到正理想解的距离
d2 = np.linalg.norm(b-cm, axis=1)  #求到负理想解的距离
f = d2 / (d1+d2)  #计算评价值
print('评价值：', np.round(f,4))

                  
