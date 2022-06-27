#程序文件ti10_10.py
from collections import Counter
import pylab as plt

with open('ti10_10_1.txt') as f:   # 获取数据
    datalines0 = f.readlines()[7:]
datalines = [i.strip().split() for i in datalines0]
# 取出序号 (同时筛选出既有CD4浓度也有HIV的数据)
order = [i[0] for i in datalines if len(i) == 5]
# 统计每一个序号的个数
result = Counter(order)
# 筛选出大于5的数据
key_filter = list(filter(lambda k: result[k] >= 5, result))
data_dic = {}
for dataline in datalines:
    if dataline[0] in key_filter:
        data_dic[dataline[0]] = data_dic.get(dataline[0], []) +\
                                [list(map(eval, dataline[1:]))]

plt.rc('font', size=15); plt.rc('font', family='SimHei')
# 绘图CD4浓度(随机的取8个)
keys = list(data_dic.keys())[:8]
plt.subplot(121)
for keyi in keys:
    datai = data_dic[keyi]
    x = [i[0] for i in datai if len(i) == 4]
    y = [i[1] for i in datai if len(i) == 4]
    plt.plot(x, y)
plt.xlabel('$t$'); plt.ylabel('浓度')
    
plt.subplot(122)
for keyi in keys:
    datai = data_dic[keyi]
    print(datai)
    x = [i[2] for i in datai if len(i) == 4]
    y = [i[3] for i in datai if len(i) == 4]
    plt.plot(x, y)
plt.xlabel('$t$'); plt.ylabel('浓度')
plt.show()
