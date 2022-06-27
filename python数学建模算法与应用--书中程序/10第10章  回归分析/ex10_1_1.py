#程序文件ex10_1.py
import numpy as np
import statsmodels.api as sm
import pylab as plt

def check(d):
    x0 = d[0]; y0 = d[1]; d ={'x':x0, 'y':y0}
    re = sm.formula.ols('y~x', d).fit() #拟合线性回归模型
    print(re.summary())
    print(re.outlier_test())  #输出已知数据的野值检验
    print('残差的方差', re.mse_resid)
    pre=re.get_prediction(d)
    df = pre.summary_frame(alpha=0.05)
    dfv = df.values; low, upp = dfv[:,4:].T  #置信下限上限
    r = (upp-low)/2  #置信半径
    num = np.arange(1, len(x0)+1)
    plt.errorbar(num, re.resid, r, fmt='o')
    plt.show()
a = np.loadtxt('data10_1.txt')
plt.rc('font', size=15); plt.plot(a[0], a[1], 'o')
plt.figure(); check(a)
a2 = a; a2 = np.delete(a2, 8, axis=1)  #删除第9列
check(a2); a3 = a2
a3 = np.delete(a3, 4, axis=1); check(a3)

