# 获得hard case和easy case的视频名称列表
# hard_or_easy 
#   |—————— easy.txt
#   |—————— hard.txt

# 运行前需要运行 pre.py


import os

import time
import pandas as pd
from matplotlib import pyplot as plt

import datetime

import CluBearSmartVendor as csv 
#--------------------------------------------------------------------------
csv.set_global_python_path('/root/miniconda3/envs/myconda/bin/python')

#--------------------------------------------------------------------------
name_list1 = os.listdir('/database/datasets/SmartVender/video8000')
name_list2 = os.listdir('/database/datasets/SmartVender/video12000')

hard_or_easy_dir = os.path.join(os.getcwd(),"hard_or_easy")
os.makedirs(hard_or_easy_dir,exist_ok = True)

def gen_video_path(video_dir,name_list):
    for i in name_list:
        yield os.path.join(video_dir,i)
        

with open(os.path.join(hard_or_easy_dir,"hard_case.txt"),"a") as f1,open(os.path.join(hard_or_easy_dir,"easy_case.txt"),"a") as f2:
    f1.write(str(datetime.datetime.now())+'\n'),f2.write(str(datetime.datetime.now())+'\n')
    
for video_path in gen_video_path('/database/datasets/SmartVender/video8000',name_list1[0:5]):
    print(video_path.split("/")[-1])
    flag = csv.extract(video_path)[0][0]
    print(flag)
    if flag == "否":
        with open(os.path.join(hard_or_easy_dir,"hard_case.txt"),"a") as f:
            f.write(video_path+'\n')
    else:
        with open(os.path.join(hard_or_easy_dir,"easy_case.txt"),"a") as f:
            f.write(video_path+'\n')
        
        
# [getattr(dataset, 'frame', 0) - 1, tid, tlwh[0], tlwh[1], tlwh[2], tlwh[3], t.score]

