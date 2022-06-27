#程序文件ex14_4.py
import numpy as np

a = np.loadtxt('data14_4.txt')
f1 = lambda x: x/8800
f2 = lambda x: 1-x/8000
f3 = lambda x: (x<=5.5)+(8-x)/(8-5.5)*((x>5.5) & (x<8))
f4 = lambda x: 1-x/200
f5 = lambda x: (x-50)/(1500-50)
R = []
for i in range(len(a)):
    s = 'f'+str(i+1)+'(a['+str(i)+'])'; R.append(eval(s))
R = np.array(R)
w = np.array([0.25, 0.2, 0.2, 0.1, 0.25])
B = w @ R   #计算综合评价值
print('评价值：', np.round(B,4))
