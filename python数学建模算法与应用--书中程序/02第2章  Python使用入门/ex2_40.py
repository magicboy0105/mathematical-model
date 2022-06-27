#程序文件ex2_40.py
import pandas as pd
import numpy as np
d=pd.DataFrame(np.random.randint(1,6,(10,4)), columns=list("ABCD"))
d1=d[:4]  #获取前4行数据
d2=d[4:]  #获取第5行以后的数据
dd=pd.concat([d1,d2])   #数据行合并
s1=d.groupby('A').mean()      #数据分组求均值
s2=d.groupby('A').apply(sum)  #数据分组求和
