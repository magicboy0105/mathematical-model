#程序文件ex15_8_2.py
import numpy as np

p = np.array([[0.8, 0.1, 0.1],[0.5, 0.1, 0.4],[0.5, 0.3, 0.2]])
val, vec = np.linalg.eig(p.T)
s = vec[:,0] / sum(vec[:,0])  #最大特征值对应的特征向量归一化
print('求得特征向量为：', np.round(s,4))
