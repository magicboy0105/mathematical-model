#程序文件ex2_19.py
import numpy.random as nr
x1=list(range(9,21))
nr.shuffle(x1)       #shuffle()用来随机打乱顺序
x2=sorted(x1)        #按照从小到大排序
x3=sorted(x1,reverse=True)  #按照从大到小排序
x4=sorted(x1,key=lambda item:len(str(item)))  #以指定的规则排序
print(x1); print(x2); print(x3); print(x4)
