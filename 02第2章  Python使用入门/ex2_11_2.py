#程序文件ex2_11_2.py
import string, random, collections  #依次加载三个模块
x=string.ascii_letters+string.digits
y=''.join([random.choice(x) for i in range(1000)])
count=collections.Counter(y)
for k,v in sorted(count.items()):
    print(k, ':', v)

