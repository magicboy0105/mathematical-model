#程序文件ti8_9.py
r = 0.0036; N = 360; Q = 400000
x = round((1+r)**N*Q*r/((1+r)**N-1),2)
xt = x*N  #总还款额
print('x=',x); print('xt=',xt)
