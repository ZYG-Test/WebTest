#导包
import unittest
import time
from tools.BStestRunner import BSTestRunner

# 定义测试套件为所有测试用例
suite = unittest.defaultTestLoader.discover("./",pattern="test_shop*.py")

#报告生成目录及文件名称
dir_path = '../report/{}.html'.format(time.strftime("%Y_%m_%d %H_%M_%S"))

#获取文件流并调用run运行测试套件
with open(dir_path,'wb')as f:
    BSTestRunner(stream=f,title="web自动化测试报告",description="操作系统：win10").run(suite)