#程序文件ex2_5_1.py
import os
fn=[filename for filename in
    os.listdir('D:\Programs\Python\Python37')
    if filename.endswith(('.exe','.py'))]
print(fn)
