from cloudshell.networking.huawei.huawei_cli_handler import HuaweiCliHandler
from cloudshell.networking.huawei.flows.huawei_add_vlan_flow import HuaweiAddVlanFlow
from cloudshell.networking.huawei.flows.huawei_remove_vlan_flow import HuaweiRemoveVlanFlow
from cloudshell.networking.devices.runners.connectivity_runner import ConnectivityRunner


class HuaweiConnectivityRunner(ConnectivityRunner):
    def __init__(self, cli, logger, api, context):
        """
        Handle add/remove vlan flows

        :param cli:
        :param logger:
        :param api:
        :param context:
        """

        super(HuaweiConnectivityRunner, self).__init__(logger)
        self._cli_handler = HuaweiCliHandler(cli, context, logger, api)
        self.add_vlan_flow = HuaweiAddVlanFlow(cli_handler=self._cli_handler,
                                              logger=self._logger)
        self.remove_vlan_flow = HuaweiRemoveVlanFlow(cli_handler=self._cli_handler,
                                                    logger=self._logger)
