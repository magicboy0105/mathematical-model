#程序文件ex10_10.py
import numpy as np
b=np.loadtxt("data10_7_2.txt")
odds9=np.exp(b@[1,9])
odds9vs8=np.exp(b@[1,9])/np.exp(b@[1,8])
print("odds9=%.4f,odds9vs8=%.4f"%(odds9,odds9vs8))


