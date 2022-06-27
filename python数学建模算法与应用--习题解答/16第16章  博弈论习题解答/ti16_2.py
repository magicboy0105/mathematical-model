#程序文件ti16_2.py
from scipy.optimize import fsolve
import numpy as np

eq1 = lambda x: [0.58*x[0]+0.93*x[1]-0.95*x[0]-0.70*x[1],sum(x)-1]
eq2 = lambda y: [0.58*y[0]+0.95*y[1]-0.93*y[0]-0.70*y[1],sum(y)-1]
x = fsolve(eq1,[1,1]); y = fsolve(eq2,[0,0])
print('罚球队员最优策略：', np.round(x,4))
print('守门队员最优策略：', np.round(y,4))
print('对策值V=', round([0.58,0.93]@x, 4))
