from cloudshell.networking.huawei.huawei_cli_handler import HuaweiCliHandler
from cloudshell.networking.devices.runners.state_runner import StateRunner


class HuaweiStateRunner(StateRunner):
    def __init__(self, cli, logger, api, context):
        """

        :param cli:
        :param logger:
        :param api:
        :param context:
        """

        super(HuaweiStateRunner, self).__init__(logger, api, context)
        self._cli_handler = HuaweiCliHandler(cli, context, logger, api)
