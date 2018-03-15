# -*- coding: utf-8 -*-
__author__ = 'ljm'
__date__ = '2018/3/10 21:53'

import os
import sys

from scrapy import cmdline

# 创建我们的调试工具类
# 将系统当前目录设置为项目根目录
# os.path.abspath(__file__)               # 为当前文件所在绝对路径
# os.path.dirname(__file__)               # 为文件所在目录
# D:\imooc\articlespider\main.py
# D:\imooc\articlespider
# print(os.path.dirname(os.path.abspath(__file__)))
# 执行命令，相当于在控制台cmd输入改名了
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute(['scrapy', 'crawl', 'jobbole'])
