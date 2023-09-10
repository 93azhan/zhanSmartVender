# 请在git上查阅SHA为f31f528e714a62b2704a4f642d7a2c030cb2db6b的commit，在mydetect中会保存selected_track
# 保存selected_track


import os
import time
import pandas as pd
from matplotlib import pyplot as plt

import datetime

import CluBearSmartVendor as csv 
#--------------------------------------------------------------------------

csv.set_global_python_path('/root/miniconda3/envs/myconda/bin/python')

#--------------------------------------------------------------------------

hard_or_easy_dir = os.path.join(os.getcwd(),"hard_or_easy")
os.makedirs(hard_or_easy_dir,exist_ok = True)

def gen_video_path(video_dir,name_list):
    for i in name_list:
        yield os.path.join(video_dir,i)

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
    else :
        with open("ERROR.txt","a") as f:
            f.write(name+'\n')
        continue
    flag = csv.extract(video_path)[0][0]
    print(flag)
    if flag == "否":
        with open(os.path.join(hard_or_easy_dir,"hard_case.txt"),"a") as f:
            f.write(video_path+'\n')
    else:
        with open(os.path.join(hard_or_easy_dir,"easy_case.txt"),"a") as f:
            f.write(video_path+'\n')