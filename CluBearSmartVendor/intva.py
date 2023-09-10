'''集成各分类器'''

from .va0 import detector
from .va1 import type_classifier
from .va2 import cap_classifier
from .va3 import bottle_classifier
from .va4 import belt_classifier, liquid_classifier

from pathlib import Path
import sys
import shutil
import os
import time


    
class integrated_classifier(object):

    def __init__(self,):
        # 当前工作目录
        self.tmp_path = os.getcwd()
        
        # 生成细分分类器
        self.myclassifier = type_classifier() # 瓶身信息
        self.mycap = cap_classifier() # 瓶盖信息
        self.mybottle = bottle_classifier() # 瓶体类型
        self.mybelt = belt_classifier() # 腰带特征
        self.myliquid = liquid_classifier() # 液体颜色
        print('All classifiers are compiled')
        
        # 是否汇报概率
        self.prob_return = False
    
    def set_python_path(self, python_path):
        # 统一设置python执行器路径
        self.myclassifier.python_path = python_path
        self.mycap.python_path = python_path
        self.mybottle.python_path = python_path
        self.mybelt.python_path = python_path
        self.myliquid.python_path = python_path
        
    def detect(self, img_path):
        if not isinstance(img_path,str): print('The pathfile must be a str.'); return
        if not os.path.exists(img_path): print('This file does not exist!'); return
        if not os.path.isfile(img_path): print('This is not a file!'); return
            
        t0 = time.time()
        echo = []
        prob = []
        result = self.myclassifier.detect(img_path) # 瓶身信息 va1      
        for i in range(len(result)):
            echo.append(result[i][0])
            prob.append(result[i][1])
            
        (cap_res, cap_prob) = self.mycap.detect(img_path) # 瓶盖信息 va2
        echo.append(cap_res)
        prob.append(cap_prob)
        
        (bottle_res, bottle_prob) = self.mybottle.detect(img_path) # 瓶身信息 va3
        echo.append(bottle_res)
        prob.append(bottle_prob)
        
        (belt_res, belt_prob) = self.mybelt.detect(img_path) # 腰带特征 va4
        echo.append(belt_res)
        prob.append(belt_prob)
        
        (liquid_res, liquid_prob) = self.myliquid.detect(img_path) # 瓶身信息 va4
        echo.append(liquid_res)
        prob.append(liquid_prob)   
        t1 = time.time()
        print('All classifications finished. %.4fs' % (t1-t0))
        
        if self.prob_return:
            return echo, prob
        else:
            return echo
        
        
    def truncatedir(self, _dir):
        shutil.rmtree(_dir)
        os.mkdir(_dir)
        
    def fresh(self):
        '''清空中间文件'''
        
        FILE = Path(__file__).resolve()
        yolo5_zj_path = str(FILE.parents[0]) + '/YOLOv5_zj'  

        yolo5_ch_path = str(FILE.parents[0]) + '/YOLOv5_ch'
        
        # 清理
        self.truncatedir(yolo5_zj_path + '/runs/detect/')
        self.truncatedir(yolo5_ch_path + '/runs/detect/')
        

# 集成检测分类器
mydetector = detector()
worker = integrated_classifier()  
python_path = '/root/miniconda3/envs/myconda/bin/python'
worker.set_python_path(python_path)
mydetector.python_path = python_path

def set_global_python_path(new_python_path):
    # 若环境中python执行器的路径改变，可用该方法进行更新
    global python_path
    python_path = new_python_path 
    worker.set_python_path(python_path)
    mydetector.python_path = python_path

def extract(video_path, is_prob=False,clear_result=True):
    global worker
    global mydetector
    
    if not isinstance(video_path,str): print('CSV: The pathfile must be a str.'); return
    if not os.path.exists(video_path): print('CSV: This file does not exist!'); return
    if not os.path.isfile(video_path): print('CSV: This is not a file!'); return    
    

    '''1.从视频提取图片'''

    try:
        easycase_res = mydetector.detect(video_path)
    except:
        print("================An exception occurred!================")
        print("================An exception occurred!================")
        print("================An exception occurred!================")
        print("================An exception occurred!================")
        print("================An exception occurred!================")
        print("================An exception occurred!================")
    
    if easycase_res == None:
        # 未获取 easy_case

        detect_res = ['否', '/', '/', '/', '/', '/', '/', '/', '/', '/']
        
        prob = [1.0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                
        # 清理存储的最大物框图片
        clear_result and worker.fresh()
        if is_prob:
            return [detect_res, prob, None]
        else:
            return [detect_res, None]

    else:
            
        [out_img_path, output_img_dir, max_image] = easycase_res
        '''2.提取图片特征'''
        if is_prob:
            worker.prob_return = True
            detect_res, prob = worker.detect(out_img_path)
        else:
            worker.prob_return = False
            detect_res = worker.detect(out_img_path)

        # 清理存储的最大物框图片
        if clear_result:
            shutil.rmtree(output_img_dir)
            worker.fresh()
 
        if is_prob:
            return [['是'] + detect_res, [1.0] + prob, max_image]
        else:
            return [['是'] + detect_res, max_image]
       
        
    

    
        
        
        
        
        