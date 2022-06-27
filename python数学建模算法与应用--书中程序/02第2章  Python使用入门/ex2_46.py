#程序文件ex2_46.py
from scipy.integrate import quad
def fun46(x, a, b):
    return a*x**2+b*x
I1 = quad(fun46, 0, 1, args=(2, 1))
I2 = quad(fun46, 0, 1, args=(2, 10))
print(I1); print(I2)

