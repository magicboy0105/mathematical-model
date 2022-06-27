#程序文件ex11_12.py
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_val_score

a=pd.read_excel("data11_10.xlsx",header=None)
b=a.values; x0=b[:-2,:-1].astype(float)
y0=b[:-2,-1].astype(float)
md = LDA(); print(cross_val_score(md, x0, y0,cv=2))



    

    
