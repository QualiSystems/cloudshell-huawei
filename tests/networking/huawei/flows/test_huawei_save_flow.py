#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import mock

from cloudshell.networking.huawei.flows.huawei_save_flow import HuaweiSaveFlow


class TestHuaweiSaveFlow(unittest.TestCase):
    def setUp(self):
        cli_handler = mock.MagicMock()
        logger = mock.MagicMock()
        super(TestHuaweiSaveFlow, self).setUp()
        self.tested_instance = HuaweiSaveFlow(
            cli_handler=cli_handler, logger=logger, file_system="flash"
        )

    def tearDown(self):
        super(TestHuaweiSaveFlow, self).tearDown()
        del self.tested_instance

    def test_execute_flow_fail_unexpected_config_type(self):
        """ Failed due to unexpected configuration type """

        folder_path = "tftp://127.0.0.1/Quali_Tests"

        with self.assertRaisesRegexp(Exception, "Device doesn't support saving"):
            self.tested_instance.execute_flow(folder_path, "unexpected-config")

    @mock.patch("cloudshell.networking.huawei.flows.huawei_save_flow.SystemActions")
    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_save_flow.SaveRestoreActions"
    )
    def test_execute_flow_success_startup_remote(
        self, save_actions_class, system_actions_class
    ):
        """ Successfully save startup configuration """

        folder_path = "tftp://127.0.0.1/quali_test_startup"

        save_actions = mock.MagicMock()
        save_actions_class.return_value = save_actions

        sys_actions = mock.MagicMock()
        system_actions_class.return_value = sys_actions
        sys_actions.display_startup_config.return_value = """MainBoard:
  Configured startup system software:        flash:/CE6850EI-V100R005C10SPC200.cc
  Startup system software:                   flash:/CE6850EI-V100R005C10SPC200.cc
  Next startup system software:              flash:/CE6850EI-V100R005C10SPC200.cc
  Startup saved-configuration file:          flash:/vrpcfg.zip
  Next startup saved-configuration file:     flash:/vrpcfg.zip
  Startup paf file:                          default
  Next startup paf file:                     default
  Startup patch package:                     flash:/CE6850EI-V100R005SPH005.PAT
  Next startup patch package:                flash:/CE6850EI-V100R005SPH005.PAT"""

        self.tested_instance.execute_flow(folder_path, "startup")

        save_actions.put_file.assert_called_once_with(
            server_address="127.0.0.1",
            src_file="flash:/vrpcfg.zip",
            dst_file="quali_test_startup",
        )


# if configuration_type == "running-config":
#     # src_file = "{file_system}:/qualirunconfig.cfg".format(file_system=self.FILE_SYSTEM)
#     src_file = "quali_run_config.cfg"
#     save_action.save_runninig_config(dst_file=src_file)
# else:
#     startup_config = system_action.display_startup_config()
#     src_file = save_action.get_startup_config_filename(startup_config=startup_config)
#
# scheme = url.get(UrlParser.SCHEME).lower()
#
# if (not scheme or scheme == self.FILE_SYSTEM) and src_file != folder_path:
#     save_action.copy_file(src_file=src_file, dst_file=folder_path)
# elif scheme in ["ftp", "tftp"]:
#     save_action.put_file(server_address=url.get(UrlParser.HOSTNAME),
#                          src_file=src_file,
#                          dst_file=url.get(UrlParser.FILENAME))
# else:
#     raise Exception("Unsupported backup protocol {scheme}. "
#                     "Supported types are ftp, tftp of local({file_system})".format(scheme=scheme,
#                                                                                    file_system=self.FILE_SYSTEM))


"""display startup
MainBoard:
  Configured startup system software:        flash:/CE6850EI-V100R005C10SPC200.cc
  Startup system software:                   flash:/CE6850EI-V100R005C10SPC200.cc
  Next startup system software:              flash:/CE6850EI-V100R005C10SPC200.cc
  Startup saved-configuration file:          flash:/vrpcfg.zip
  Next startup saved-configuration file:     flash:/vrpcfg.zip
  Startup paf file:                          default
  Next startup paf file:                     default
  Startup patch package:                     flash:/CE6850EI-V100R005SPH005.PAT
  Next startup patch package:                flash:/CE6850EI-V100R005SPH005.PAT

  Next startup saved-configuration file:(?P<startup>.*)




  >display version
Huawei Versatile Routing Platform Software
VRP (R) software, Version 8.100 (CE6850EI V100R005C10SPC200)
Copyright (C) 2012-2015 Huawei Technologies Co., Ltd.
HUAWEI CE6850-48S4Q-EI uptime is 155 days, 8 hours, 47 minutes
Patch Version: V100R005SPH005

CE6850-48S4Q-EI(Master) 1 : uptime is  155 days, 8 hours, 47 minutes
        StartupTime 2018/10/31   16:08:18+12:00
Memory    Size    : 2048 M bytes
Flash     Size    : 1024 M bytes
NVRAM     Size    : 512  K bytes
CE6850-48S4Q-EI version information
1. PCB    Version : CEM48S4QP01    VER C
2. MAB    Version : 1
3. Board  Type    : CE6850-48S4Q-EI
4. CPLD1  Version : 108
5. CPLD2  Version : 108
6. BIOS   Version : 312
"""
