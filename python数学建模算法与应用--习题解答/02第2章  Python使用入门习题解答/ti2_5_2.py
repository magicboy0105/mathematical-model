#程序文件ti2_5_1.py
import pylab as plt
import numpy as np

x=np.linspace(-4,4,50)
y=np.linspace(-5,5,50)
x,y=np.meshgrid(x,y)
z=x**2/4+y**2/6
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z,cmap='winter'); plt.show()
