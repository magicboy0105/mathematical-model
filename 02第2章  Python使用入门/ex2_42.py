#程序文件ex2_42.py
with open('data2_2.txt') as fp:
    L1=[]; L2=[];
    for line in fp:
        L1.append(len(line))
        L2.append(len(line.strip()))  #去掉换行符
data = [str(num)+'\t' for num in L2]  #转换为字符串
print(L1); print(L2)
with open('data2_42.txt', 'w') as fp2:
    fp2.writelines(data)
