#1.导包
import unittest

#2.自定义测试类，继承unittest模块中的TestCase类即可
class TestDemo1(unittest.TestCase):
#3.测试方法，必须以test_开头
    def test_method1(self):
        print('你好')

    def test_method2(self):
        print('我好')
#4.执行测试用例（方法）