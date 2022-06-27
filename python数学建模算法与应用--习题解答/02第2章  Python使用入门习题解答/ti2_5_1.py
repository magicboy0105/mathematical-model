#程序文件ti2_5_1.py
import pylab as plt
import numpy as np

u=np.linspace(0,2*np.pi,50)
v=np.linspace(-np.pi/2,np.pi/2,50)
u,v=np.meshgrid(u,v)
x=2*np.cosh(v)*np.cos(u)
y=np.sqrt(10)*np.cosh(v)*np.sin(u)
z=2*np.sqrt(2)*np.sinh(v)
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z); plt.show()
