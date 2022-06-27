#程序文件ex8_16.py
Q = 300000; r = 0.051 /12; N = 360
x = round((1+r)**N*Q*r/((1+r)**N-1),2)
print(x); print(x*N)

