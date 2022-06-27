#程序文件ti7_5.py
import numpy as np

d=np.loadtxt('ti7_5.txt')
x=d[0]; y=d[1]; xb=x.mean(); yb=y.mean()
ah=sum((x-xb)*(y-yb))/sum((x-xb)**2)  #求a的估计值
bh=yb-ah*xb                           #求b的估计值
print('a,b估计值为：', round(ah,4), round(bh,4))

