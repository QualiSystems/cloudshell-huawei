from cloudshell.networking.cisco.cisco_cli_handler import CiscoCliHandler
from cloudshell.networking.cisco.flow.cisco_autoload_flow import CiscoAutoloadFlow
from cloudshell.networking.cisco.ios.autoload.cisco_ios_autoload import CiscoIOSAutoload
from cloudshell.networking.devices.runners.autoload_runner import AutoloadRunner


class AutoloadRunner(AutoloadRunner):
    def __init__(self, cli, logger, api, context, supported_os):
        super(AutoloadRunner, self).__init__(cli, logger, context, supported_os)
        self._cli_handler = CiscoCliHandler(cli, context, logger, api)
        self._logger = logger
        self._autoload_flow = CiscoAutoloadFlow(cli_handler=self._cli_handler,
                                                autoload_class=CiscoIOSAutoload,
                                                logger=logger,
                                                resource_name=self._resource_name)
