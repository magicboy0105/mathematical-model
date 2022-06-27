#程序文件ex15_10.py
from sklearn.linear_model import Perceptron
import numpy as np

x0=np.array([[-0.5,-0.5,0.3,0.0],[-0.5,0.5,-0.5,1.0]]).T
y0=np.array([1,1,0,0])
md = Perceptron().fit(x0,y0)   #构造并拟合模型
print('模型系数和常数项分别为：', md.coef_,',',md.intercept_)  
print('模型精度：',md.score(x0,y0))   #模型检验
print('预测值为：',md.predict([[-0.5,0.2]]))
