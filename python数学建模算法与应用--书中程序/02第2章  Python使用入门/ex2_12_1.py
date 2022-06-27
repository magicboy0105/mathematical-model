#程序文件ex2_12_1.py
def factorial(n):  #定义阶乘函数
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r
def fib(n):   #定义输出斐波那契数列函数
    a, b = 1, 1
    while a < n:
        print(a, end='  ')
        a, b = b, a+b

print('%d!=%d'%(5,factorial(5)))
fib(200)
