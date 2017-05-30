import unittest

import mock

from cloudshell.networking.huawei.runners.huawei_configuration_runner import HuaweiConfigurationRunner


class TestHuaweiAutoloadRunner(unittest.TestCase):
    def setUp(self):
        self.autoload_runner = HuaweiConfigurationRunner(cli=mock.MagicMock(),
                                                         logger=mock.MagicMock(),
                                                         context=mock.MagicMock(),
                                                         api=mock.MagicMock())
