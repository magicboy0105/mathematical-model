#程序文件ex17_4.py
import numpy as np

f = lambda x,y: np.log((1+x)**2+y**2)
u = np.zeros((4,4)); m = 4; n = 4; h = 1/3
u[0,:] = f(0,np.arange(m)*h)
u[-1,:] = f(1, np.arange(m)*h)
u[:,0] = f(np.arange(n)*h,0)
u[:,-1] = f(np.arange(n)*h,1)
b = -np.array([u[1,0]+u[0,1],u[3,1]+u[2,0],u[1,3]+u[0,2],u[2,3]+u[3,2]])
a = np.array([[-4,1,1,0],[1,-4,0,1],[1,0,-4,1],[0,1,1,-4]])
x = np.linalg.inv(a) @ b
print('解x:', np.round(x,4))

