import json
import unittest
from parameterized import parameterized
from tools1 import login1


# 必须是[(),()]或者[[],[]]格式

# 定义死的参数
# data=[
# ('admin','123456','登录成功'),
# ('root','123456','登录失败'),
# ('admin','123123','登录失败')
# ]


def buile_data():
    with open('info1.json',encoding='utf-8') as f:
        data = []
        result = json.load(f)  # 现在是[{},{},{}]
        for i in result:  # i为{}
            data.append((i.get('username'),i.get('password'),i.get('expect')))
    return data


# 定义测试类
class TestLogin(unittest.TestCase):
    # 书写测试方法(用到的测试数据用变量代替)
    # @parameterized.expand(data)#用装饰器传参
    @parameterized.expand(buile_data())
    def test_login(self,username,password,expect):
        self.assertEqual(expect,login1(username,password))






#知识点：跳过

import unittest
version=20
class TestDemo(unittest.TestCase):
    @unittest.skip('不执行')
    def test_1(self):
        print('测试方法1')
    @unittest.skipIf(version>=30,'版本大于等于30,不用测试')
    def test_2(self):
        print('测试方法2')
    def test_3(self):
        print('测试方法3')