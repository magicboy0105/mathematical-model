#程序文件ti4_9_1.py
import cvxpy as cp
import numpy as np

s=[]  #切割模式初始化
r=[]  #每种切割模式余料初始化
for i in range(3):
    for j in range(4):
        for k in range(7):
            if 2.9*i+2.1*j+k>5.9 and 2.9*i+2.1*j+k<=6.9:
                    s.append([i,j, k])
                    r.append(6.9-2.9*i-2.1*j-k)
a=np.array(s).T; r=np.array(r)
ind=np.argsort(r)  #r中元素从小到大排列的地址
a=a[:,ind]; r=r[ind]
x=cp.Variable(7, integer=True)
obj1=cp.Minimize(sum(x))
con=[a@x>=100, x>=0]
prob1=cp.Problem(obj1, con)
prob1.solve(solver='GLPK_MI')
print('最优值为：', prob1.value)
print('最优解为：\n', x.value)
print('余料长度为：\n', r@x.value)
print('三种短钢管的数量为：', a@x.value)

obj2=cp.Minimize(r@x)
prob2=cp.Problem(obj2, con)
prob2.solve(solver='GLPK_MI')
print('---------\n最优值为：', prob2.value)
print('最优解为：\n', x.value)
print('余料长度为：\n', r@x.value)
print('三种短钢管的数量为：', a@x.value)
np.savetxt('data4_9_1.txt', a, fmt='%4.0f')
np.savetxt('data4_9_2.txt', r, fmt='%4.1f')


