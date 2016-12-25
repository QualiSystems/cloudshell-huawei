import re
import time

from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.networking.huawei.huawei_command_modes import  EnableCommandMode, DefaultCommandMode, ConfigCommandMode
from cloudshell.networking.cli_handler_impl import CliHandlerImpl
from cloudshell.shell.core.api_utils import decrypt_password_from_attribute


class HuaweiCliHandler(CliHandlerImpl):
    def __init__(self, cli, context, logger, api):
        try:
            super(HuaweiCliHandler, self).__init__(cli, context, logger, api)
            modes = CommandModeHelper.create_command_mode(context)
            self.default_mode = modes[DefaultCommandMode]
            self.enable_mode = modes[EnableCommandMode]
            self.config_mode = modes[ConfigCommandMode]
            self.logger=logger
        except Exception as e:
            print e

    def on_session_start(self, session, logger=None):
        """Send default commands to configure/clear session outputs
        :return:
        """
        print logger
        self._enter_config_mode(session, self.logger)
        session.hardware_expect('user-interface console 0', ConfigCommandMode.PROMPT, logger)
        session.hardware_expect('screen-length 0', ConfigCommandMode.PROMPT,logger)
        session.hardware_expect('quit', ConfigCommandMode.PROMPT, logger)
        session.hardware_expect('quit', DefaultCommandMode.PROMPT, logger)


    def _enter_config_mode(self, session, logger=None):
        max_retries = 5
        error_message = 'Failed to enter config mode, please check logs, for details'
        output = session.hardware_expect(ConfigCommandMode.ENTER_COMMAND,
                                         '{0}|{1}'.format(ConfigCommandMode.PROMPT, EnableCommandMode.PROMPT), logger)

        if not re.search(ConfigCommandMode.PROMPT, output):
            retries = 0
            while not re.search(r"[Cc]onfiguration [Ll]ocked", output, re.IGNORECASE) or retries == max_retries:
                time.sleep(5)
                output = session.hardware_expect(ConfigCommandMode.ENTER_COMMAND,
                                                 '{0}|{1}'.format(ConfigCommandMode.PROMPT, EnableCommandMode.PROMPT),
                                                 logger)
            if not re.search(ConfigCommandMode.PROMPT, output):
                raise Exception('_enter_config_mode', error_message)

    def enter_enable_mode(self, session, logger=None):
        """
        Enter enable mode

        :param session:
        :param logger:
        :raise Exception:
        """
        result = session.hardware_expect('', '{0}|{1}'.format(DefaultCommandMode.PROMPT, EnableCommandMode.PROMPT),
                                         logger)
        if not re.search(EnableCommandMode.PROMPT, result):
            enable_password = decrypt_password_from_attribute(api=self._api,
                                                              password_attribute_name='Enable Password',
                                                              context=self._context)
            expect_map = {'[Pp]assword': lambda session, logger: session.send_line(enable_password, logger)}
            session.hardware_expect('enable', EnableCommandMode.PROMPT, action_map=expect_map, logger=logger)
            result = session.hardware_expect('', '{0}|{1}'.format(DefaultCommandMode.PROMPT, EnableCommandMode.PROMPT),
                                             logger)
            if not re.search(EnableCommandMode.PROMPT, result):
                raise Exception('enter_enable_mode', 'Enable password is incorrect')
