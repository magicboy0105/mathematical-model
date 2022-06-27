#程序文件ex2_23.py
def filter_non_unique(L):
    return [item for item in L if L.count(item) == 1]
a=filter_non_unique([1, 2, 2, 3, 4, 4, 5])
print(a)
