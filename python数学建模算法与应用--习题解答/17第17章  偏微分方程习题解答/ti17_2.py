#程序文件ti17_2.py
import numpy as np
from scipy import sparse
import pylab as plt

M = 50; N = 60  #空间和时间的点数 
x0 = 0; xL = 1; dx = (xL - x0)/(M - 1)    #空间步长
t0 = 0; tF = 0.2; dt = (tF - t0)/(N - 1)  #时间步长
D = 0.5; alpha = -5  #扩散系数和反应率
r = dt*D/dx**2; s = dt*alpha; a = 1 + 2*r - s
xspan = np.linspace(x0, xL, M)
tspan = np.linspace(t0, tF, N)
main_diag = (1 + 2*r - s)*np.ones(M)
off_diag = -r*np.ones(M-1)
diagonals = [main_diag, off_diag, off_diag]
A = sparse.diags(diagonals, [0,-1,1], shape=(M,M)).toarray()
A[0,1] = -2*r; A[M-1,M-2] = -2*r

U = np.zeros((M, N))  #解的初始化
U[:,0] = 4*xspan - 4*xspan**2  #初值条件
leftBC = np.arange(1, N+1)
f = np.sin(leftBC*np.pi/2)
rightBC = np.arange(1, N+1)
g = np.sin(3*rightBC*np.pi/4)
for k in range(1, N):
    c = np.zeros(M-2)
    b1 = np.array([2*r*dx*f[k], 2*r*dx*g[k]])
    b1 = np.insert(b1, 1, c); b2 = U[0:M, k-1]
    b = b1 + b2  #线性方程组常数项
    U[0:M, k] = np.linalg.solve(A,b)  #解线性方程组
print('所求的数值解为：\n', U)

plt.rc('text', usetex=True); plt.rc('font', size=15)
X, T = np.meshgrid(tspan, xspan)
ax = plt.axes(projection='3d')
ax.plot_surface(X, T, U, linewidth=0, cmap=plt.cm.coolwarm)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticks([0, 0.05, 0.1, 0.15, 0.2])
ax.set_xlabel('$t$'); ax.set_ylabel('$x$')
ax.set_zlabel('$u$'); plt.tight_layout(); plt.show()
