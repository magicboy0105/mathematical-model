#程序文件ti6_7.py
import numpy as np
import pandas as pd
import networkx as nx
import pylab as plt

a=pd.read_excel('ti6_7.xlsx'); b=a.values
s=b[:,0]; ss=list(s)      #提取顶点字符串
x=b[:,1].astype(float)    #提出x坐标
y=b[:,2].astype(float)    #提取y坐标
num=b[:,3].astype(float)  #提取顶点类别
ad=b[:,4:].astype(str)    #提取邻接顶点
in1=np.where(num==1)[0]   #提取第1类点的编号
in2=np.where(num==2)[0]   #提取第2类点的编号
in3=np.where(np.isnan(num))[0]

plt.plot(x[in1],y[in1],'Pk')
plt.text(x[in1]+10,y[in1],dict(zip(range(len(in1)),s[in1])))

plt.show()
