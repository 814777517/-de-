#TestLoaderc的使用,配合case里的test02
import unittest
#实例化加载对象并添加用例
suite=unittest.TestLoader().discover('./case','*test02*')
#实例化运行对象
runner=unittest.TextTestRunner()
runner.run(suite)

#注:这种只能测一个用例的那种






