# 根据所有.json文件，得到的anchor的数量，判断属于哪一类hard case


import os
import json


with open("jsonlist.txt","r") as f:
    allHard = f.readlines()
    allHard = [i.rstrip("\n") for i in allHard]
print(len(allHard))

first = 0
second = 0
for name in allHard:
    video_path = os.path.join('/mnt/yingqiu/selected_track',name)
    with open(video_path,"r") as f:
        result = json.load(f)
        if len(result) == 0:
            first += 1
        else :
            second+=1
            
print(f'first:{first}')
print(f'second:{second}')