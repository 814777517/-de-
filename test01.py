import unittest

from test import Test

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test))
runner=unittest.TextTestRunner()
runner.run(suite)






#