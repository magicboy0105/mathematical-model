#程序文件ex2_53.py
import pandas as pd
import pylab as plt
plt.rc('font',family='SimHei')  #用来正常显示中文标签
plt.rc('font',size=16)  #设置显示字体大小
a=pd.read_excel("data2_52.xlsx",header=None)
b=a.T; b.plot(kind='bar'); plt.legend(['钻石', '铂金'])
plt.xticks(range(6), b[0], rotation=0)
plt.ylabel('数量'); plt.show()
