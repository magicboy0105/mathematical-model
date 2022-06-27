#程序文件名ex7_15.py
import numpy as np
from scipy.optimize import curve_fit

xy0=np.array([[6, 2, 6, 7, 4, 2, 5, 9],
              [4, 9, 5, 3, 8, 5, 8, 2]])
z0=np.array([5, 2, 1, 9, 7, 4, 3, 3])
z = lambda t, a, b, c: a*np.exp(b*t[0])+c*t[1]**2
p, pcov=curve_fit(z, xy0, z0)
print('a，b，c的拟合值为：', p)
