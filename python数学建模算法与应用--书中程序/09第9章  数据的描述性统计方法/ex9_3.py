#程序文件ex9_3.py
from scipy.stats import norm
from scipy.optimize import fsolve

c1 = norm.ppf(0.25, 3, 2)  #求0.25分位数
fc = lambda c: 1-norm.cdf(c, 3, 2)-3*norm.cdf(c, 3, 2)  #定义方程对应的匿名函数
c2 = fsolve(fc, 1)  #求初始值为1的方程零点
print('c1=', c1); print('c2=', c2)

