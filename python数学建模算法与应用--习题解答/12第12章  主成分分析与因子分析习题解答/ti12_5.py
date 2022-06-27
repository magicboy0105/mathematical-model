#程序文件ti12_5.py
import numpy as np
import pandas as pd

r = np.array([[1, 0.80, 0.37, 0.78, 0.26, 0.38],
              [0.80, 1, 0.32, 0.65, 0.18, 0.33],
              [0.37, 0.32, 1, 0.36, 0.71, 0.62],
              [0.78, 0.65, 0.36, 1, 0.18, 0.39],
              [0.26, 0.18, 0.71, 0.18, 1, 0.69],
              [0.38, 0.33, 0.62, 0.39, 0.69, 1]])
c, d = np.linalg.eig(r)  #求特征值和特征向量
ind = np.argsort(-c)     #特征值从大到小排序的地址
cc = c[ind]; dd = d[ind,:]  #重排特征值和特征向量的顺序
print('特征值为：', cc); print('特征向量为：\n', dd)
rt = cc/sum(cc)     #计算各主成分的贡献率
cr = np.cumsum(rt)  #求累积贡献率
print('各主成分的贡献率为：', rt)
f = pd.ExcelWriter('ti12_5.xlsx')
da = np.vstack([cc, rt, cr]).T
pd.DataFrame(da).to_excel(f, 'Sheet1', index=False)
pd.DataFrame(dd).to_excel(f, 'Sheet2', index=False)
f.save()
