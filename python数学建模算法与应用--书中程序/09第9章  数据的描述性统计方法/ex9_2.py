#程序文件ex9_2.py
from scipy.stats import binom
import pylab as plt

n = 6; p = 0.3
x = plt.arange(7); y = binom.pmf(x, n, p)
plt.subplot(121); plt.plot(x, y, 'ro')
plt.vlines(x, 0, y, 'k', lw=2, alpha=0.5) #vlines(x, ymin, ymax)画竖线图
#lw设置线宽度，alpha设置图的透明度
plt.subplot(122); plt.stem(x, y, use_line_collection=True)
plt.savefig("figure9_2.png", dpi=500); plt.show()


