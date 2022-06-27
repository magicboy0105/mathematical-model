#程序文件ti3_1.py
import sympy as sp
sp.var('n',positive=True,integer=True)
sp.var('p,q',positive=True)
a=sp.Matrix([[1-p,q],[p,1-q]])
print('特征值为：', a.eigenvals())
print('特征向量为：\n', a.eigenvects())
P,D=a.diagonalize()  #把a相似对角化
An=P@(D**n)@(P.inv())
xyn=An@sp.Matrix([[1],[1]])/2
xyn2=sp.simplify(xyn); print(xyn2)
