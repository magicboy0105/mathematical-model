#程序文件ti11_5.py
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_val_score as cvs

a=pd.read_excel('ti11_5.xlsx', header=None)
b=a.values; x0=b[:-3,:-1].astype(float)
y0=b[:-3,-1].astype(float)
x=b[-3:,:-1].astype(float)  #提取待判样本数据

md1=KNC().fit(x0,y0)  #构造并拟合欧氏距离模型
pre1=md1.predict(x)    #预测待判样本
print('分类结果：', pre1)
print('回代误判率：', 1-md1.score(x0,y0))
print('交叉误判率：', 1-cvs(KNC(),x0,y0,cv=4))  #计算4折交叉误判率

v=np.cov(x0.T)  #计算协方差矩阵
md2=KNC(metric='mahalanobis',metric_params={'V':v})  #构造马氏距离模型
md2.fit(x0,y0)         #拟合马氏距离模型
pre2=md2.predict(x)    #预测待判样本
print('分类结果：', pre2)
print('回代误判率：', 1-md2.score(x0,y0))

md3=LDA().fit(x0,y0)  #构造并拟合Fisher线性模型
pre3=md3.predict(x)    #预测待判样本
print('分类结果：', pre3)
print('回代误判率：', 1-md3.score(x0,y0))
print('交叉误判率：', 1-cvs(LDA(),x0,y0,cv=4))  #计算4折交叉误判率
