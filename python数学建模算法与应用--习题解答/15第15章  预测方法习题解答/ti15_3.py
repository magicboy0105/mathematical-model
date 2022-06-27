#程序文件ti15_3.py
from sklearn.neural_network import MLPRegressor
import numpy as np
import pylab as plt

a = np.loadtxt('ti15_3.txt')
x0 = a[:,:3]; y0 = a[:,3]  #提出训练样本数据
m1 = x0.max(axis=0); m2 = x0.min(axis=0)  #计算逐列最大值和最小值
bx0 = (x0-m2)/(m1-m2)  #数据标准化
#构造并拟合模型
md = MLPRegressor(solver='lbfgs',hidden_layer_sizes=10,
                  activation='identity').fit(bx0, y0)
x = np.array([[73.39,75.55],[3.9635,4.0975],[0.9880,1.0268]]).T
bx = (x-m2) / (m1-m2)  #数据标准化
yh = md.predict(bx); print('预测值为：,',np.round(yh,4))
yh0 = md.predict(bx0); delta = abs(yh0-y0)/y0*100
print('已知数据预测的相对误差：', np.round(delta,4))
t = np.arange(1990, 2010)
plt.rc('font', size=15); plt.rc('font', family='SimHei')
plt.plot(t, y0, '--o', label='原始数据')
plt.plot(t, yh0, '-*', label='预测数据')
plt.xticks(t, rotation=55); plt.legend(); plt.show()
