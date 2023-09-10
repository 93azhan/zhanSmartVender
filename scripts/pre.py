# 加载需要的包，有时需要运行两次
# 主要是cython
import os
os.chdir('/mnt/yingqiu/CluBearSmartVendor')
os.system('chmod +x libs_preparation.sh')
os.system('./libs_preparation.sh')
os.chdir('/mnt/yingqiu')