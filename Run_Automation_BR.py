import unittest
import os
from Util.BeautifulReport import BeautifulReport
if __name__ == '__main__':
    # 获取当前文件所在目录的父目录的绝对路径
    parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 定义测试集合
    test_suite = unittest.defaultTestLoader.discover('TestScript', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试报告', log_path=parent_directory_path + "\\PO\\TestResult\\Report\\")