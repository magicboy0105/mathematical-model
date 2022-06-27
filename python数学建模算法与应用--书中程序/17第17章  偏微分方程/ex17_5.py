#程序文件ex17_5.py
from scipy import sparse
from scipy.sparse.linalg import spsolve
import numpy as np
import pylab as plt

def rhs_func(x, y, M):   #定义右端项
    g = (20 * np.cos(3*np.pi*X[1:-1,1:-1]) *
         np.sin(2*np.pi*Y[1:-1,1:-1])).flatten()
    f = [g[i::M-2] for i in range(M-2)] #抽取内部值
    f = np.array(f).flatten() # 展开成((M-2)**2, )数组
    return f

def bc_dirichlet(x, y, M):  #定义Dirichlet边界条件
    lBC = y[:,0]**2; leftBC = lBC[1:M-1]
    rBC = np.ones(M); rightBC = rBC[1:M-1]
    tBC = x[0,:]**3; topBC = tBC[1:M-1]
    bBC = np.ones(M); bottomBC = bBC[1:M-1]
    g1 = np.zeros((M-2)**2)
    for i in range(M-2): g1[(M-2)*i] = topBC[i] 
    for j in range(M-2): g1[(M-2)*(j+1)-1] = bottomBC[j]
    k1 = np.zeros((len(leftBC),1)); k1[0] = 1.0
    leftBCk = sparse.kron(k1,leftBC).toarray().flatten()
    k2 = np.zeros((len(rightBC),1)); k2[-1] = 1.0
    rightBCk = sparse.kron(k2,rightBC).toarray().flatten()
    g = g1 + leftBCk + rightBCk
    return [g, lBC, tBC, rBC, bBC]

def generate_lhs_matrix(M, hx, hy):  #定义线性方程组系数矩阵
    alpha = hx**2/hy**2; n = M - 2
    main_diag = 2 * (1 + alpha) * np.ones(n)
    off_diag = -1 * np.ones(n)
    diagonals = [main_diag, off_diag, off_diag]
    B = sparse.diags(diagonals, [0, -1, 1], shape=(n,n)).toarray()
    C = sparse.diags([-1*np.ones(M)], [0],  shape=(n,n)).toarray()
    e1 = np.eye(n)
    A1 = sparse.kron(e1,B).toarray()
    e2 = sparse.diags([np.ones(M),np.ones(M)], [-1,1], shape=(n,n)).toarray()
    A2 = sparse.kron(e2,C).toarray()
    mat = A1 + A2
    return mat

M = 50; (x0, xf) = (0.0, 1.0); (y0, yf) = (0.0, 1.0)
hx = (xf - x0)/(M-1); hy = (yf - y0)/(M-1)
x1 = np.linspace(x0, xf, M); y1 = np.linspace(y0, yf, M)
X, Y = np.meshgrid(x1, y1)   #生成网格数据
frhs = rhs_func(X, Y, M)     #右端项的值
fbc = bc_dirichlet(X, Y, M)  #边界条件值
rhs = frhs*(hx**2) + fbc[0]
A = generate_lhs_matrix(M, hx, hy)
V = np.linalg.solve(A,rhs)  #解线性方程组
V = V.reshape((M-2, M-2)).T
U = np.zeros((M,M))  #初始化
U[1:M-1, 1:M-1] = V
U[:,0] = fbc[1]; U[0,:] = fbc[2]
U[:,M-1] = fbc[3]; U[M-1,:] = fbc[4]
print('所求的数值解为：\n',U)

plt.rc('text', usetex=True); plt.rc('font', size=15)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, U, cmap=plt.cm.coolwarm)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$u$'); plt.tight_layout()
ax.view_init(20, -106); plt.show()
