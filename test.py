##练习题   配合test01和tools
import unittest

from tools import add


class Test(unittest.TestCase):
    def test_add(self):
        if add(1,2)==3:
            print('测试通过')

        else:
            print('测试不通过')
