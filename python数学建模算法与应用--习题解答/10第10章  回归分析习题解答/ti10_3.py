#程序文件ti10_3.py
import numpy as np
import statsmodels.api as sm

a=np.loadtxt('ti10_3.txt')  #表中数据后面补充两个0
x=a[::2]; x=x[np.nonzero(x)]; n=len(x)
y=a[1::2]; y=y[np.nonzero(y)]
p1=np.polyfit(x,y,1)  #拟合一次多项式
yh1=np.polyval(p1,x)  #计算预测值
s1=sum((y-yh1)**2)/(n-2)  #计算残差的方差
p2=np.polyfit(x,y,2)  #拟合二次多项式
yh2=np.polyval(p2,x)  #计算预测值
s2=sum((y-yh2)**2)/(n-3)  #计算残差的方差
mat1=np.vstack([np.ones(n),1/x]).T  #构造系数矩阵
p3=np.linalg.pinv(mat1)@(1/y)  #线性最小二乘法拟合参数
yh3=1/(mat1@p3)  #求双曲线函数的预测值
s3=sum((y-yh3)**2)/(n-2)  #计算残差方差
mat2=np.vstack([np.ones(n),np.log(x)]).T
p4=np.linalg.pinv(mat2)@y  #线性最小二乘法拟合参数
yh4=mat2@p4   #求对数函数的预测值
s4=sum((y-yh4)**2)/(n-2)  #计算残差方差
print('残差方差分别为：', np.round([s1,s2,s3,s4],4))
