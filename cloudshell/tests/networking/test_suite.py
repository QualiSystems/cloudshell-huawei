import sys
import unittest

sys.path.append("/")
sys.path.append("../")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'test_'
    suite = loader.discover("huawei/test_configuration_operations", pattern='test_*.py')

    allTests = unittest.TestSuite(suite)
    runner.run(allTests)