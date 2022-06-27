#程序文件ti14_2.py
import numpy as np

a = np.loadtxt('ti14_2.txt').T; m,n = a.shape
m1 = a.max(axis=0); m2 = a.min(axis=0)  #逐列求最大值和最小值
b = (a-m2)/(m1-m2)  #所有指标值都按效益型标准化
for j in [1,2,3]:  #成本型指标值额外处理
    b[:, j] = (m1[j]-a[:,j])/(m1[j]-m2[j])
ck = b.max(axis=0)  #求参考数列
t = ck - b  #求参考数列与每一个比较数列的差
z1 = t.max(); z2 = t.min()  #求两级最大差和最小差
rho = 0.5   #分辨系数
xs = (z2+rho*z1)/(t+rho*z1)  #计算灰色关联系数
r = xs.mean(axis=1)  #计算关联度
ind = np.argsort(-r)+1  #从大到小排列的地址
print('灰色关联度：', np.round(r,4))

                  
