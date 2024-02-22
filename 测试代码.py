#1.导包
import unittest

from 测试 import TestDemo
from 测试1 import TestDemo1

#2.创建套件对象
suite=unittest.TestSuite()
#3.使用套件对象添加用例方法
suite.addTest(TestDemo('test_method1'))
suite.addTest(TestDemo('test_method2'))
suite.addTest(TestDemo1('test_method1'))
suite.addTest(TestDemo1('test_method2'))
#简便：跟上面效果相同，套件对象.addTest(unittest.makeSuite(测试类名)
suite.addTest(unittest.makeSuite(TestDemo))
suite.addTest(unittest.makeSuite(TestDemo1))
#4.实例化运行对象
runner=unittest.TextTestRunner()
#5.使用运行对象去打印套件对象
#运行对象.run(套件对象)
runner.run(suite)














