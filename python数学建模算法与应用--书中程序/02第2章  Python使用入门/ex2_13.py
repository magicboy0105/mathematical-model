#程序文件ex2_13.py
def bifurcate_by(L, fn):
    return [[x for x in L if fn(x)],
            [x for x in L if not fn(x)]]
s=bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
print(s)
