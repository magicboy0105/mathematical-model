#程序文件ex2_52.py
import pandas as pd
import pylab as plt
plt.rc('font',family='SimHei')  #用来正常显示中文标签
plt.rc('font',size=16)  #设置显示字体大小
a=pd.read_excel("data2_52.xlsx", header=None)
b=a.values  #提取其中的数据
x=b[0]; y=b[1:]
plt.plot(x,y[0],'-*b',label='钻石')
plt.plot(x,y[1],'--dr',label='铂金')
plt.xlabel('月份'); plt.ylabel('每月销量')
plt.legend(loc='upper left'); plt.grid(); plt.show()
