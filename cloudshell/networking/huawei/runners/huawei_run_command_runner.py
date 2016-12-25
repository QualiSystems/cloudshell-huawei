from cloudshell.networking.huawei.huawei_cli_handler import HuaweiCliHandler
from cloudshell.networking.devices.runners.run_command_runner import RunCommandRunner


class HuaweiRunCommandRunner(RunCommandRunner):
    def __init__(self, cli, context, logger, api):
        """

        :param context: command context
        :param api: cloudshell api object
        :param cli: CLI object
        :param logger: QsLogger object
        :return:
        """

        super(HuaweiRunCommandRunner, self).__init__(logger)
        self._cli_handler = HuaweiCliHandler(cli, context, logger, api)
