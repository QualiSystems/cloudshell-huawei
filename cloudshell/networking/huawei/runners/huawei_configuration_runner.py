from cloudshell.networking.huawei.huawei_cli_handler import HuaweiCliHandler
from cloudshell.networking.huawei.flows.huawei_restore_flow import HuaweiRestoreFlow
from cloudshell.networking.huawei.flows.huawei_save_flow import HuaweiSaveFlow
from cloudshell.networking.devices.runners.configuration_runner import ConfigurationRunner


class HuaweiConfigurationRunner(ConfigurationRunner):
    def __init__(self, cli, logger, context, api):
        super(HuaweiConfigurationRunner, self).__init__(logger, context, api)
        self._cli_handler = HuaweiCliHandler(cli, context, logger, api)
        self._save_flow = HuaweiSaveFlow(cli_handler=self._cli_handler,
                                        logger=self._logger)
        self._restore_flow = HuaweiRestoreFlow(cli_handler=self._cli_handler,
                                              logger=self._logger)
        self.file_system = 'flash:'
