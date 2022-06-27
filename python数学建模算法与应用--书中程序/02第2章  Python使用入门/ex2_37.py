#程序文件ex2_37.py
import pandas as pd
import numpy as np
dates=pd.date_range(start='20191101',end='20191124',freq='D')
a1=pd.DataFrame(np.random.randn(24,4), index=dates, columns=list('ABCD'))
a2=pd.DataFrame(np.random.rand(24,4))
