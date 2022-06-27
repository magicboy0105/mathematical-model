#程序文件ex2_29.py
import numpy as np
a = np.arange(16).reshape(4,4)  #生成4行4列的数组
b = np.vsplit(a, 2)             #行分割
print('行分割：\n', b[0], '\n', b[1])
c = np.hsplit(a, 4)             #列分割
print('列分割：\n', c[0], '\n', c[1], '\n', c[2], '\n', c[3])
