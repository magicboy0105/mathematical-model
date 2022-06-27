#程序文件ex3_6_1.py
import numpy as np
import pandas as pd

a = np.loadtxt('data3_6_1.txt')
b = 0.5 * np.corrcoef(a.T) + 0.5  #求归一化的相似度
c= pd.DataFrame(b)
c.to_excel('data3_6_2.xlsx', index=False)

print('请输入人员编号1-18')
user = int(input())
n = a.shape[1]  #变量的个数
no = np.where(a[user-1, :]==0)[0] #未评分编号
yb = set(range(n)) - set(no)  #已评分编号
yb = list(yb)
ys = a[user-1, yb]  #已评分分数
sc = np.zeros(len(no))  #初始化
for i in range(len(no)):
    sim = b[no[i], yb]
    sc[i] = ys @ sim / sum(sim)
print('未评分项的编号为：', no+1)
print('未评分项的分数为：', np.round(sc, 4))
    
