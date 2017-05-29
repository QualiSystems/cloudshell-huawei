# from unittest import TestCase
# from mock import MagicMock
# from cloudshell.networking.huawei.huawei_configuration_operations import HuaweiConfigurationOperations
# import re, time
#
#
# def _get_time_stamp():
#     return time.strftime("%d%m%y-%H%M%S", time.localtime())
#
#
# res = '''MainBoard:
#   Configured startup system software:        flash:/s5710-x-li-v200r008c00spc500.cc
#   Startup system software:                   flash:/s5710-x-li-v200r008c00spc500.cc
#   Next startup system software:              flash:/s5710-x-li-v200r008c00spc500.cc
#   Startup saved-configuration file:          flash:/vrpcfg.zip
#   Next startup saved-configuration file:     flash:/vrpcfg.zip
#   Startup paf file:                          default
#   Next startup paf file:                     default
#   Startup license file:                      default
#   Next startup license file:                 default
#   Startup patch package:                     NULL
#   Next startup patch package:                NULL'''
#
#
# class TestHuaweiConfiguration(TestCase):
#     def _get_handler(self):
#         self.cli = MagicMock()
#         self.snmp = MagicMock()
#         self.api = MagicMock()
#         self.logger = MagicMock()
#         return HuaweiConfigurationOperations(cli=self.cli, logger=self.logger, api=self.api,
#                                              resource_name='Huawei37')
#
#     def test_save_validates_destination_host_host_parameter(self):
#         handler = self._get_handler()
#         handler.cli.send_command = MagicMock(return_value=res)
#
#         response_template = '{0}-{1}-{2}'.format('Huawei37', "startup",
#                                                  _get_time_stamp())
#         response = handler.save_configuration('flash:/', "startup")
#
#         self.assertTrue(re.search(response_template, response))
#
#     def test_save_config(self):
#         resource_name = 'Huawei37'
#
#         handler = self._get_handler()
#         handler.resource_name = resource_name
#
#         response_template = '{0}-{1}-{2}'.format(resource_name, "running",
#                                                  _get_time_stamp())
#         print response_template
#         handler.cli.send_command = MagicMock(return_value=res)
#         response = handler.save_configuration('flash:/', "running")
#         self.assertIsNotNone(response)
#         print response_template
#         print response
#         self.assertTrue(re.search(response_template, response))
