
from cloudshell.cli.command_mode import CommandMode


class DefaultCommandMode(CommandMode):
    PROMPT = '<.*?>'
    ENTER_COMMAND = ''
    EXIT_COMMAND = 'quit'


    def __init__(self, context):
        """
        Default command mode

        :param context:
        """
        self._context = context
        CommandMode.__init__(self, DefaultCommandMode.PROMPT, DefaultCommandMode.ENTER_COMMAND,
                             DefaultCommandMode.EXIT_COMMAND)


class EnableCommandMode(CommandMode):
    PROMPT = r'<.*?>'
    ENTER_COMMAND = '' # system-view
    EXIT_COMMAND = 'quit'

    def __init__(self, context):
        """
        Initialize Enable command mode - supper command mode for huawei

        :param context:
        """
        self._context = context

        CommandMode.__init__(self, EnableCommandMode.PROMPT, EnableCommandMode.ENTER_COMMAND,
                             EnableCommandMode.EXIT_COMMAND)


class ConfigCommandMode(CommandMode):
    PROMPT = r'\[.*?\]'
    ENTER_COMMAND = 'sys'
    EXIT_COMMAND = 'quit'

    def __init__(self, context):
        """
        Initialize Config command mode

        :param context:
        """
        exit_action_map = {
            self.PROMPT: lambda session, logger: session.send_line('quit', logger)}
        CommandMode.__init__(self, ConfigCommandMode.PROMPT,
                             ConfigCommandMode.ENTER_COMMAND,
                             ConfigCommandMode.EXIT_COMMAND,
                             exit_action_map=exit_action_map)


CommandMode.RELATIONS_DICT = {
    DefaultCommandMode: {
        EnableCommandMode: {
            ConfigCommandMode: {}
        }
    }
}