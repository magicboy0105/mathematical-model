#程序文件ex2_54.py
import pylab as plt
import numpy as np
plt.rc('text', usetex=True)  #调用tex字库
y1=np.random.randint(2, 5, 6);
y1=y1/sum(y1); plt.subplot(2, 2, 1);
str=['Apple', 'grape', 'peach', 'pear', 'banana', 'pineapple']
plt.barh(str,y1)  #水平条形图
plt.subplot(222); plt.pie(y1, labels=str)  #饼图
plt.subplot(212)
x2=np.linspace(0.01, 10, 100); y2=np.sin(10*x2)/x2
plt.plot(x2,y2); plt.xlabel('$x$')
plt.ylabel('$\\mathrm{sin}(10x)/x$'); plt.show()
