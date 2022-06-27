#程序文件ex14_5.py
import numpy as np
import cvxpy as cp

d = np.loadtxt('data14_5.txt')
a = d[:,:3]; b = d[:,3:]
u = cp.Variable(3, pos=True); v = cp.Variable(2, pos=True)
for j in range(10):
    con = [ a @ u >= b @ v, a[j] @ u ==1]
    obj = cp.Maximize(b[j]@v)
    prob = cp.Problem(obj, con)
    prob.solve(solver='GLPK_MI')
    print('第',str(j+1),'个对象最优值：',round(prob.value,4))
    print('最优解：\n', np.round(u.value,4),'\n', np.round(v.value,4))


