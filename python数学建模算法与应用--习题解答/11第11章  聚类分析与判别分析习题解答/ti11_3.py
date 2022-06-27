#程序文件ti11_3.py
import numpy as np
from scipy.stats import zscore
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_val_score as cvs

a=np.loadtxt('ti11_3.txt')
m=a.shape[0]; b=zscore(a); x=b[8:,:]
x0=b[:8,:]; y0=np.hstack([np.ones(3),2*np.ones(5)])

x1=b[:3,:]; mu1=x1.mean(axis=0)
x2=b[3:8,:]; mu2=x2.mean(axis=0); D=[]
for i in x:
    d1 = np.linalg.norm(i-mu1)
    d2 = np.linalg.norm(i-mu2)
    D.append([d1, d2])
ind1 = np.argmin(D, axis=1)+1
print('分类结果：', ind1)
check =[]  #存放已知样本点的马氏距离
for i in x0:
    d1 = np.linalg.norm(i-mu1)
    d2 = np.linalg.norm(i-mu2)
    check.append([d1, d2])
ind2 = np.argmin(check, axis=1)+1
rate = sum(y0-ind2)/len(y0) #计算误判率
print('回代误判率：', rate)

#下面直接调用库函数
md2=KNC().fit(x0,y0)  #构造并拟合欧氏距离模型
pre2=md2.predict(x)   #预测待判样本
print('分类结果:', pre2)
print('回代误判率：', 1-md2.score(x0,y0))
print('交叉误判率：',1-cvs(KNC(),x0,y0,cv=3))  #计算3折交叉误判率

md3=LDA().fit(x0,y0)  #构造并拟合Fisher线性模型
pre3=md3.predict(x)   #预测待判样本
print('分类结果：', pre3)
print('回代误判率：', 1-md3.score(x0,y0))
print('交叉误判率：',1-cvs(LDA(),x0,y0,cv=3))  #计算3折交叉误判率
