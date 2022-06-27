#程序文件ex2_11_1.py
import string
import random
x=string.ascii_letters+string.digits
y=''.join([random.choice(x) for i in range(1000)])
#choice()用于从多个元素中随机选择一个
d=dict()  #构造空字典
for ch in y:
    d[ch]=d.get(ch,0)+1;
for k,v in sorted(d.items()):
    print(k,':',v)
