#1.导包
import unittest




#2.自定义测试类，继承unittest模块中的TestCase类即可
class TestDemo(unittest.TestCase):
#3.测试方法，必须以test_开头
    def test_method1(self):
        print('愤怒的')

    def test_method2(self):
        print('房东房客就')
#4.执行测试用例（方法）















