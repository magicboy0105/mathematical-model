#程序文件ex15_6.py
import numpy as np

with open('data15_6.txt') as f:
    s = f.read().replace(' ','').replace('\n','')
a = np.zeros((4,4))  #统计数据初始化
mfind = lambda s,c: [x for x in range(s.find(c), len(s)) if s[x:x+2] == c]
for i in range(1,5):
    for j in range(1,5):
        a[i-1,j-1] = len(mfind(s,str(i)+str(j)))
print('统计数据矩阵a:\n', a); print('a的行和：',a.sum(axis=1))

