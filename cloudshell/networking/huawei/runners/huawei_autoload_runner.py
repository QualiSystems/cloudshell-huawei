from cloudshell.networking.huawei.huawei_cli_handler import HuaweiCliHandler
from cloudshell.networking.huawei.flows.huawei_autoload_flow import HuaweiAutoloadFlow
from cloudshell.networking.huawei.autoload.huawei_generic_snmp_autoload import HuaweiGenericSNMPAutoload
from cloudshell.networking.devices.runners.autoload_runner import AutoloadRunner


class HuaweiAutoloadRunner(AutoloadRunner):
    def __init__(self, cli, logger, api, context, supported_os):
        super(HuaweiAutoloadRunner, self).__init__(cli, logger, context, supported_os)
        self._cli_handler = HuaweiCliHandler(cli, context, logger, api)
        self._logger = logger
        self._autoload_flow = HuaweiAutoloadFlow(cli_handler=self._cli_handler,
                                                autoload_class=HuaweiGenericSNMPAutoload,
                                                logger=logger,
                                                resource_name=self._resource_name)
