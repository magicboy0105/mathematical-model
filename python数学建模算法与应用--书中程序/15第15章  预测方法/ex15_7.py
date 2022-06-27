#程序文件ex15_7.py
import numpy as np

P1 = np.mat([0.2, 0.4, 0.4])
P = np.mat([[0.8, 0.1, 0.1],[0.5, 0.1, 0.4],[0.5, 0.3, 0.2]])
P4 = P1 @ P ** 3  
print('P4:', P4)
