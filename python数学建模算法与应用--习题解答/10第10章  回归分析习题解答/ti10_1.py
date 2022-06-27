#程序文件ti10_1.py
import numpy as np
import pylab as plt
import pandas as pd
import statsmodels.api as sm

a=pd.read_excel('ti10_1.xlsx', header=None)
a=a.values; t0=a[::2]; t0=t0[~np.isnan(t0)]
x0=a[1::2]; x0=x0[~np.isnan(x0)]
plt.scatter(t0,x0); plt.show()
d={'t':t0,'x':x0}; md=sm.formula.ols('x~t',d).fit()
print(md.summary()); print('残差的方差', md.mse_resid)
