#程序文件ti10_7.py
import numpy as np

a = np.loadtxt('ti10_7.txt')      #提取10×8矩阵
d = np.vstack([a[:,:4], a[:,4:]]) #变形为20×4矩阵
f = d[:,3] * (d[:,2]==1) +(100-d[:,3])*(d[:,2]==0) #发芽频数
pd = f/100  #发芽频率
mat = np.stack([np.ones(20), d[:,0],d[:,1], d[:,0]*d[:,1]]).T
cs = np.linalg.pinv(mat) @ np.log(pd/(1-pd))  #拟合参数
print('拟合的参数为：', cs)

x11 = -(cs[0]+cs[2]) / (cs[1]+cs[3])  #计算水分含量
x10 = -cs[0] / cs[1]                  #计算水分含量
print('两种水分含量分别为：', x11,',',x10)

odd1 = np.exp(cs@[1,6,1,6]) #计算加盖时发芽的赔率
odd2 = np.exp(cs@[1,6,0,0])  #计算不加盖时发芽的赔率            
OR = odd1/odd2              #计算赔率比
print('加盖和不加盖的赔率分别为：',odd1,',',odd2)              
print('赔率比为：', OR)
