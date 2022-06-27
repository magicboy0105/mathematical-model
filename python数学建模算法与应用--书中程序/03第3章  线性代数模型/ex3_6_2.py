#程序文件ex3_6_2.py
import numpy as np
import pandas as pd

a = np.loadtxt('data3_6_1.txt')
u, sigma, vt = np.linalg.svd(a)
print(sigma)
cs = np.cumsum(sigma**2)  
rate = cs / cs[-1]  #计算信息累积贡献率
ind = np.where(rate>=0.9)[0][0]+1
#ind为奇异值的个数，满足信息提出率达到90%
b = np.diag(sigma[:ind]) @ u.T[:ind, :] @ a  #得到降维数据

c = np.linalg.norm(b, axis=0, keepdims=True)  #逐列求范数
d = 0.5 * b.T @ b / (c.T @ c) + 0.5  #求相似度
#d = 0.5 * np.corrcoef(b.T) + 0.5
dd = pd.DataFrame(d)
dd.to_excel('data3_6_3.xlsx', index=False)

print('请输入人员编号1-18')
user = int(input())
n = a.shape[1]  #变量的个数
no = np.where(a[user-1, :]==0)[0] #未评分编号
yb = set(range(n)) - set(no)  #已评分编号
yb = list(yb)
ys = a[user-1, yb]  #已评分分数
sc = np.zeros(len(no))  #初始化
for i in range(len(no)):
    sim = d[no[i], yb]
    sc[i] = ys @ sim / sum(sim)
print('未评分项的编号为：', no+1)
print('未评分项的分数为：', np.round(sc,4))
    
