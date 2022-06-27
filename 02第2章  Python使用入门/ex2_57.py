#程序文件ex2_57.py
import pylab as plt
import numpy as np
ax=plt.axes(projection='3d')
X = np.arange(-6, 6, 0.25)
Y = np.arange(-6, 6, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')
plt.colorbar(surf); plt.show()
