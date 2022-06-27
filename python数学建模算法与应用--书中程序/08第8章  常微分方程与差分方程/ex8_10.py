#程序文件ex8_10.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt

df = lambda f,t,w: [w/np.sqrt((10+20*np.cos(t)-f[0])**2+(20+
                 15*np.sin(t)-f[1])**2)*(10+20*np.cos(t)-f[0]),
                 w/np.sqrt((10+20*np.cos(t)-f[0])**2+(20+
                 15*np.sin(t)-f[1])**2)*(20+15*np.sin(t)-f[1])]
d= lambda xy,t: np.sqrt((xy[:,0]-10-20*np.cos(t))**2+
                (xy[:,1]-20-15*np.sin(t))**2)  #计算距离函数
plt.rc('font',size=16); plt.rc('text', usetex=True)
t1 = np.linspace(0, 3.4068, 100)  #终值时间是一点一点凑出来的
s1 = odeint(df, [0,0], t1, args=(20,))
d1 = d(s1, t1)  #计算两者之间的距离
plt.plot(t1, d1); plt.xlabel('$t$'); plt.ylabel('$d$', rotation=0)
plt.figure(); t2=np.linspace(0,50,501)
s2 = odeint(df, [0,0], t2, args=(5,))
d2 = d(s2, t2)  #计算两者之间的距离
plt.plot(t2, d2); plt.xlabel('$t$')
plt.ylabel('$d$', rotation=0); plt.show()
