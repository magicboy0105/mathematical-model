#程序文件ex15_11.py
from sklearn.neural_network import MLPClassifier
import numpy as np

a = np.loadtxt('data15_11.txt')
x0 = a[:10,:]; x = a[10:,:]  #提出训练样本和待判样本数据
m1 = x0.max(axis=0); m2 = x0.min(axis=0)  #计算逐列最大值和最小值
bx0 = (x0-m2)/(m1-m2)  #数据标准化
bx0[:,1] = (m1[1]-x0[:,1])/(m1[1]-m2[1])   #x2值特殊处理
y0 = np.hstack([np.zeros(5), np.ones(5)])  #标号值
#构造并拟合模型
md = MLPClassifier(solver='lbfgs',activation='logistic',
                   hidden_layer_sizes=30).fit(bx0, y0)
bx = (x-m2) / (m1-m2)  #待判样本数据标准化
bx[:,1] = (m1[1]-x[:,1])/(m1[1]-m2[1])   #x2值特殊处理
yh = md.predict(bx); print('待判样本类别：,',yh)
print('属于各个类别的概率：\n', md.predict_proba(bx))
print('训练样本的回代准确率：', md.score(bx0, y0))
