import sys
import unittest

sys.path.append("/")
sys.path.append("../")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    loader = unittest.TestLoader()
    loader.testMethodPrefix = 'test_'
    suite = loader.discover("test_connectivity", pattern='test_apply_connectivity_changes.py')

    allTests = unittest.TestSuite(suite)
    runner.run(allTests)