#程序文件ti17_1.py
from scipy import sparse
import numpy as np
import pylab as plt

def rhs_func(X, Y, M):    #定义右端项
    g = (20 * np.cos(3*np.pi*X) * np.sin(2*np.pi*Y)).flatten()
    f = [g[i::M] for i in range(M)]
    f = np.asarray(f).flatten()
    return f
  
def generate_lhs_matrix(M, hx, hy):   #定义线性方程组系数矩阵
    alpha = hx**2/hy**2
    main_diag = 2*(1+alpha)*np.ones(M)
    off_diag = -1*np.ones(M-1)
    diagonals = [main_diag, off_diag, off_diag]
    B = sparse.diags(diagonals, [0,-1,1], shape=(M,M)).toarray()
    B[0,1] = -2.0
    D = sparse.diags([-np.ones(M+1)], [0], shape=(M,M)).toarray()
    C = sparse.diags([-2*np.ones(M+1)], [0], shape=(M,M)).toarray()
    e1 = np.eye(M); A1 = sparse.kron(e1,B).toarray()
    e2 = sparse.diags([np.ones(M),np.ones(M)], [-1,1], shape=(M,M)).toarray()
    e2[0,1] = 0.0; e2[M-1,M-2] = 0.0
    A2 = sparse.kron(e2,D).toarray()
    e3 = sparse.diags([np.ones(M),np.ones(M)], [-1,1], shape=(M,M)).toarray()
    e3[1:M-1,0:M] = 0.0
    A3 = sparse.kron(e3,C).toarray()
    mat = A1 + A2 + A3
    return mat
    
M = 50; (x0, xf) = (0.0, 1.0); (y0, yf) = (0.0, 1.0)
hx = (xf - x0)/(M-1); hy = (yf - y0)/(M-1)
X, Y = np.meshgrid(np.linspace(x0, xf, M), np.linspace(y0, yf, M))
f = rhs_func(X, Y, M)
A = generate_lhs_matrix(M, hx, hy)
U = np.linalg.solve(A,f*(hx**2))  #解线性方程组
U = U.reshape((M,M)).T
print('所求的数值解为：\n', U)

plt.rc('text', usetex=True); plt.rc('font', size=15)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, U, cmap=plt.cm.coolwarm)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$u$'); plt.tight_layout()
ax.view_init(31, -131); plt.show()
