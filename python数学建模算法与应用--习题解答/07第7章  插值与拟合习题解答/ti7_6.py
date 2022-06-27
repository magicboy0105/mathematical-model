#程序文件ti7_6.py
import numpy as np

p=[8,5,2,-1]; x0=np.linspace(-6,6,100)
y0=np.polyval(p,x0)         #计算对应的函数值
p1=np.polyfit(x0,y0,3)      #无噪声数据拟合
np.random.seed(2)           #进行一致性比较
yr=y0+np.random.randn(100)  #生成噪声数据
p2=np.polyfit(x0,yr,3)      #有噪声数据拟合
print('p1=', p1); print('p2=',np.round(p2,4))
