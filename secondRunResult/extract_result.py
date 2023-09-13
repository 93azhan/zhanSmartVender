import os
n_t = 0
n_f = 0
# 当前目录下的result.txt文件
with open("result.txt","r") as f:
    l = f.read()
    for c in l:
        if c=="T":
            n_t+=1
        if c=="F":
            n_f+=1
print(f'T:{n_t},F:{n_f},rate:{n_t/(n_t+n_f)}')