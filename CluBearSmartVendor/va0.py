'''周静老师团队'''

import pandas as pd
import numpy as np
import os
import sys
import time
from pathlib import Path
import cv2
import numpy as np
import re

#warnings.filterwarnings("ignore")

class detector(object):

    def __init__(self,):
        # 当前工作目录
        self.tmp_path = os.getcwd()
        # 编译器目录
        self.python_path = '/root/miniconda3/envs/myconda/bin/python'
        # Yolo5目录
        FILE = Path(__file__).resolve()
        self.yolo5_path = str(FILE.parents[0]) + '/YOLOv5_zj'  # YOLOv5 root directory

        # 获取文件名的pattern
        self.pat = re.compile(r'/([^/]+)\.')
        
    def detect(self, video_path):
        if not isinstance(video_path,str): print('The pathfile must be a str.'); return
        if not os.path.exists(video_path): print('This file does not exist!'); return
        if not os.path.isfile(video_path): print('This is not a file!'); return
        
        
            
        print('---------------------Start----------------------------------')
        
        t0 = time.time()
        filename = self.pat.findall(video_path)[0]
        # 命令行执行 yolo+botsort detect
        c = f'{self.python_path} {self.yolo5_path}/mydetect.py --source {video_path} --tmpdir {self.tmp_path} --save_result --save --save-txt'

        res = os.popen(c)
        resrd = res.read()
    
        t1 = time.time()
        print('-------------------Detection finished(%.4fs)--------------------' % (t1-t0))   
        
        # 输出图片存储地址
        out_img_path = f'{self.tmp_path}/image_results/{filename}.jpg'
        # 输出图片存储路径
        img_dir = f'{self.tmp_path}/image_results/'
        
        # 图片内容数据
        try:
            image = cv2.imread(out_img_path)
            max_image = image[:, :, ::-1]
            return [out_img_path, img_dir, max_image]
        except:
            print("-----------------------------------------Hard case or Nothing detected.-----------------------------------------")
            print("-----------------------------------------Hard case or Nothing detected.-----------------------------------------")
            return None
        
    """-------------------------------multiple images detection------------------------------------------------------"""
    
    def multiple_detect(self, video_path):
        #======================使用时需要加上“zhan”参数==============================================================
        if not isinstance(video_path,str): print('The pathfile must be a str.'); return
        if not os.path.exists(video_path): print('This file does not exist!'); return
        if not os.path.isfile(video_path): print('This is not a file!'); return
        
        
            
        print('---------------------Start----------------------------------')
        
        t0 = time.time()
        filename = self.pat.findall(video_path)[0]
        # 命令行执行 yolo+botsort detect
        c = f'{self.python_path} {self.yolo5_path}/mydetect.py --source {video_path} --tmpdir {self.tmp_path} --save_result --save --save-txt --del_file --zhan'

        res = os.popen(c)
        resrd = res.read()
    
        t1 = time.time()
        print('-------------------Detection finished(%.4fs)--------------------' % (t1-t0))   
        
        # 输出图片存储地址
        out_img_path = f'{self.tmp_path}/image_results/{filename}.jpg'
        # 输出图片存储路径
        img_dir = f'{self.tmp_path}/image_results/'
        
        # 图片内容数据
        try:
            image = cv2.imread(out_img_path)
            max_image = image[:, :, ::-1]
            return [out_img_path, img_dir, max_image]
        except:
            print("-----------------------------------------Hard case or Nothing detected.-----------------------------------------")
            print("-----------------------------------------Hard case or Nothing detected.-----------------------------------------")
            return None
        
        
        