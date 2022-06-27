#程序文件ex9_1.py
from scipy.stats import expon, gamma
import pylab as plt

x = plt.linspace(0, 3, 100)
L = [1/3, 1, 2]
s1 = ['*-', '.-', 'o-']
s2 = ['$\\theta=\\frac{1}{3}$','$\\theta=1$', '$\\theta=2$']
plt.rc('text', usetex=True); plt.rc('font', size=15)
plt.subplots_adjust(wspace=0.5)
plt.subplot(121)
for i in range(len(L)):
    plt.plot(x, gamma.pdf(x, 1, scale=L[i]), s1[i], label=s2[i])
plt.xlabel('$x$'); plt.ylabel('$f(x)$'); plt.legend()
plt.subplot(122)
for i in range(len(L)):
    plt.plot(x, expon.pdf(x, scale=L[i]), s1[i], label=s2[i])
plt.xlabel('$x$'); plt.ylabel('$f(x)$')
plt.legend(); plt.show()
