# 获取绝对路径
# 结果在fullHARD.txt文件中

import os

name_list1 = os.listdir('/database/datasets/SmartVender/video8000')
name_list2 = os.listdir('/database/datasets/SmartVender/video12000')
with open("HARD.txt","r") as f:
    allHard = f.readlines()
    allHard = [i.rstrip("\n")+".mp4" for i in allHard]
for name in allHard:
    if name in name_list1:
        video_path = os.path.join('/database/datasets/SmartVender/video8000',name)
    elif name in name_list2:
        video_path = os.path.join('/database/datasets/SmartVender/video12000',name)
    with open("fullHARD.txt","a") as f:
        f.write(video_path+'\n')
    