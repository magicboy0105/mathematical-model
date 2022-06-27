#程序文件ex2_22.py
a = filter(lambda x: x>10,[1,11,2,45,7,6,13])
b = filter(lambda x: x.isalnum(),['abc', 'xy12', '***'])
#isalnum()是测试是否为字母或数字的方法
print(list(a)); print(list(b))
