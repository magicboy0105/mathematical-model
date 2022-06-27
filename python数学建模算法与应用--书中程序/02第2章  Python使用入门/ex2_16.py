#程序文件ex2_16.py
from random import sample
from numpy.random import randint
a=sample(range(10),5)  #在[0,9]区间上选择不重复的5个整数
b=randint(0,10,5)      #在[0,9]区间上生成5个随机整数
print(a); print(b) 
