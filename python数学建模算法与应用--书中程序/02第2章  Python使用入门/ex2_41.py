#程序文件ex2_41.py
import pandas as pd
import numpy as np
a = pd.DataFrame(np.random.randint(1,6,(5,3)),
                 index=['a', 'b', 'c', 'd', 'e'],
                 columns=['one', 'two', 'three'])
a.loc['a', 'one'] = np.nan  #修改第1行第1列的数据
b = a.iloc[1:3, 0:2].values  #提取第2、3行，第1、2列数据
a['four'] = 'bar'  #增加第4列数据
a2 = a.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
a3 = a2.dropna()   #删除有不确定值的行
