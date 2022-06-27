#程序文件ex5_2.py
import sympy as sp
import pylab as plt

plt.rc('text', usetex=True)  #使用LaTeX字体
plt.rc('font',size=14)
sp.var('x1, x2')  #定义符号变量
y = (339-0.01*x1-0.003*x2)*x1+(399-0.004*x1-0.01*x2)*x2-(400000+195*x1+225*x2)
y = sp.simplify(y)   #化简
dy1 = y.diff(x1)     #求关于x1的偏导
dy2 = y.diff(x2)     #求关于x2的偏导
s = sp.solve([dy1, dy2], [x1, x2])
x10 = round(float(s[x1]))   #取整
x20 = round(float(s[x2]))
y0 = y.subs({x1: x10, x2: x20})  #符号函数代入数值
f = sp.lambdify('x1, x2', y, 'numpy')  #符号函数转换为匿名函数
x = plt.linspace(0, 10000, 100)
X, Y = plt.meshgrid(x, x)  #转换为网格数据
Z = f(X, Y)
ax=plt.subplot(121, projection='3d')  #第一个子窗口三维画图
ax.plot_surface(X, Y, Z,cmap='viridis')
ax.set_xlabel('$x_1$'); ax.set_ylabel('$x_2$')
plt.subplot(122)  #激活第二个子窗口
contr=plt.contour(X,Y,Z,10)  #10条等高线
plt.clabel(contr)   #等高线标注
plt.ylabel('$x_2$',rotation=0)
plt.xlabel('$x_1$')

sp.var('a', pos=True)  #定义灵敏度分析的符号参数
y = (339-a*x1-0.003*x2)*x1+(399-0.004*x1-0.01*x2)*x2-(400000+195*x1+225*x2)
y = sp.simplify(y)   #化简
dy1 = y.diff(x1)     #求关于x1的偏导
dy2 = y.diff(x2)     #求关于x2的偏导
s = sp.solve([dy1, dy2], [x1, x2])
sx1 = s[x1]; sx2 = s[x2]  #提取解分量
s1 = sp.lambdify('a', sx1, 'numpy')  #符号函数转换为匿名函数
s2 = sp.lambdify('a', sx2, 'numpy')
a0 = plt.linspace(0.002, 0.02, 50)
plt.figure()
plt.subplots_adjust(wspace = 0.65)
plt.subplot(121); plt.plot(a0, s1(a0))
plt.xlabel('$a$'); plt.ylabel('$x_1$')
plt.subplot(122); plt.plot(a0, s2(a0))
plt.xlabel('$a$'); plt.ylabel('$x_2$')
dx1 = sx1.diff(a); dx10 = dx1.subs(a, 0.01)
sx1a = dx10 * 0.01 / 4735
dx2 = sx2.diff(a); dx20 = dx2.subs(a, 0.01)
sx2a = dx20 * 0.01 / 7043
Y = y.subs({x1: s[x1], x2: s[x2]})  #求关于a的目标函数
Y = sp.factor(Y); Y = sp.simplify(Y)
Ya = sp.lambdify('a', Y, 'numpy')  #转换为匿名函数
a0 = plt.linspace(0.002, 0.02, 1000)
plt.figure(); plt.plot(a0, Ya(a0))
plt.xlabel('$a$'); plt.ylabel('$y$', rotation=0)
Sya = - 4735 ** 2 * 0.01 / 553641.025
y2 = y.subs({x1: 4735, x2: 7043, a: 0.011})  #计算近似最优利润
y3 = Y.subs(a, 0.011)   #计算最优利润
delta = (y3 - y2) / y2  #计算利润的相对误差
plt.show()

