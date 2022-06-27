#程序文件ex17_6.py
import numpy as np
from scipy import sparse
import pylab as plt

M = 50; N = 60  #空间和时间的点数
x0 = 0; xL = 1; dx = (xL - x0)/(M - 1)    #空间步长
t0 = 0; tF = 0.2; dt = (tF - t0)/(N - 1)  #时间步长
D = 0.1; alpha = -3  #扩散系数和反应率
r = dt*D/dx**2; s = dt*alpha;
xspan = np.linspace(x0, xL, M)
tspan = np.linspace(t0, tF, N)
main_diag = (1 + 2*r - s)*np.ones(M-2)
off_diag = -r*np.ones(M-3); n = M-2
diagonals = [main_diag, off_diag, off_diag]
A = sparse.diags(diagonals, [0,-1,1], shape=(n,n)).toarray()

U = np.zeros((M, N))  #解的初始化
U[:,0] = 4*xspan - 4*xspan**2  #初值条件
U[0,:] = 0.0; U[-1,:] = 0.0  #边界条件
for k in range(1, N):
    c = np.zeros(M-4)
    b1 = np.array([r*U[0,k], r*U[-1,k]])
    b1 = np.insert(b1, 1, c); b2 = U[1:M-1, k-1]
    b = b1 + b2  #线性方程组常数项
    U[1:M-1, k] = np.linalg.solve(A,b)  #解线性方程组

plt.rc('text', usetex=True); plt.rc('font', size=15)
X, T = np.meshgrid(tspan, xspan)
ax = plt.axes(projection='3d')
ax.plot_surface(X, T, U, linewidth=0, cmap=plt.cm.coolwarm)
ax.set_xticks([0, 0.05, 0.1, 0.15, 0.2])
ax.set_xlabel('$t$'); ax.set_ylabel('$x$')
ax.set_zlabel('$u$'); plt.tight_layout(); plt.show()
