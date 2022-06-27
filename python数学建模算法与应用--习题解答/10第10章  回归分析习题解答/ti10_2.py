#程序文件ti10_2.py
import numpy as np
import pandas as pd
import statsmodels.api as sm

a=pd.read_excel('ti10_2.xlsx', header=None)
a=a.values; x1=a[2::4,:]; x1=x1[~np.isnan(x1)]
x2=a[3::4,:]; x2=x2[~np.isnan(x2)]
y=a[1::4,:]; y=y[~np.isnan(y)]
d1=pd.DataFrame({'y':y,'x1':x1,'x2':x2})
md1=sm.formula.ols('y~x1+x2',d1).fit()
print(md1.summary()); print('残差的方差', md1.mse_resid)
print(md1.outlier_test())  #输出已知数据的野值检验
d2=d1.drop(20)  #删除序号为20的野值数据
md2=sm.formula.ols('y~x1+x2',d2).fit()
print(md2.summary()); print('残差的方差', md2.mse_resid)
print(md2.outlier_test())  #输出已知数据的野值检验
