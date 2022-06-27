#程序文件ex2_55.py
import pylab as plt
import numpy as np
ax=plt.axes(projection='3d')  #设置三维图形模式
z=np.linspace(-50, 50, 1000)
x=z**2*np.sin(z); y=z**2*np.cos(z)
plt.plot(x, y, z, 'k'); plt.show()
