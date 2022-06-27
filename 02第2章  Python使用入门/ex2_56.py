#程序文件ex2_56.py
import pylab as plt
import numpy as np
x=np.linspace(-4,4,100);
x,y=np.meshgrid(x,x)
z=50*np.sin(x+y);
ax=plt.axes(projection='3d')
ax.plot_surface(x, y, z, color='y')
plt.show()
