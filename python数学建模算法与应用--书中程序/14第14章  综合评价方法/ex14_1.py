#程序文件ex14_1.py
import numpy as np
import pandas as pd

a = np.loadtxt('data14_1_1.txt')
b = np.linalg.norm(a,axis=0)  #逐列求2范数
m1 = a.max(axis=0)  #逐列求最大值
m2 = a.min(axis=0)  #逐列求最小值
R1 = a / b  #全部列向量归一化处理
R2 = a / m1 #全部列向量比例变换
R3 = (a-m2) / (m1-m2)  #全部列向量极差变换
R1[:,3] = 1 - a[:,3] / b[3]  #第4列特殊处理
R2[:,3] = m2[3] / a[:,3]     #第4列特殊处理
R3[:,3] = (m1[3]-a[:,3]) / (m1[3]-m2[3])
np.savetxt('data14_1_2.txt', R1, fmt='%.4f')
f = pd.ExcelWriter('data14_1_3.xlsx')
pd.DataFrame(R1).to_excel(f, index=None)  #写入Excel文件方便做表
pd.DataFrame(R2).to_excel(f, 'Sheet2', index=None)
pd.DataFrame(R3).to_excel(f, 'Sheet3', index=None); f.save()
