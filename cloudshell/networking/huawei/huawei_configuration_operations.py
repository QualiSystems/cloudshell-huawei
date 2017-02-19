from collections import OrderedDict
import traceback
import inject
import re
import time

from cloudshell.networking.networking_utils import validateIP
from cloudshell.configuration.cloudshell_cli_binding_keys import CLI_SERVICE, CONNECTION_MANAGER
from cloudshell.networking.huawei.firmware_data.huawei_firmware_data import HuaweiFirmwareData
from cloudshell.networking.operations.interfaces.configuration_operations_interface import \
    ConfigurationOperationsInterface
from cloudshell.networking.operations.interfaces.firmware_operations_interface import FirmwareOperationsInterface
from cloudshell.shell.core.context_utils import get_resource_name


def _get_time_stamp():
    return time.strftime("%d%m%y-%H%M%S", time.localtime())


class HuaweiConfigurationOperations(ConfigurationOperationsInterface, FirmwareOperationsInterface):
    def __init__(self, cli=None, logger=None, api=None, resource_name=None):
        self._cli = cli
        self._logger = logger
        self._api = api
        try:
            self.resource_name = resource_name or get_resource_name()
        except Exception as e:
            raise Exception('HuaweiHandlerBase', 'ResourceName is empty or None')

    @property
    def logger(self):
        if self._logger is None:
            try:
                self._logger = inject.instance('logger')
            except:
                raise Exception('huawei', 'Logger is none or empty')
        return self._logger

    @property
    def api(self):
        if self._api is None:
            try:
                self._api = inject.instance('api')
            except:
                raise Exception('huawei', 'Api handler is none or empty')
        return self._api

    @property
    def cli(self):
        if self._cli is None:
            try:
                self._cli = inject.instance('cli_service')
            except:
                raise Exception('huawei', 'Cli Service is none or empty')
        return self._cli



    def get_configuration_file_name_from_device(self,configuration_type):
        if (configuration_type == 'startup'):

            command = 'display startup'
            response = self.cli.send_command(command=command)
            splitted_response = response.split("\n  ")
            if (len(splitted_response) <= 0): raise Exception('huawei',
                                                              'Upload to remote server method: no source file for startup!')

            source_file_type = splitted_response[5].split("     ")
            if (len(source_file_type) <= 0): raise Exception('huawei',
                                                             'Upload to remote server method: no source file for startup!')

            if ("Next startup saved-configuration file:" in source_file_type[0]):
                source_file = source_file_type[1]
            else:
                raise Exception('huawei', 'Upload to remote server method: no source file for startup!')

        if (configuration_type == 'running'):

            command = 'display startup'
            response = self.cli.send_command(command=command)
            splitted_response = response.split("\n  ")
            if (len(splitted_response) <= 0): raise Exception('huawei',
                                                              'Upload to remote server method: no source file for startup!')

            source_file_type = splitted_response[4].split("     ")

            if (len(source_file_type) <= 0): raise Exception('huawei',
                                                             'Upload to remote server method: no source file for startup!')

            if ("Startup saved-configuration file:" in source_file_type[0]):

                source_file = source_file_type[1]
                if(source_file==''):
                    try:
                        source_file = source_file_type[2]
                    except:
                        raise Exception('huawei', 'Upload to remote server method: no source file for running!')
                if(source_file=='NULL'):
                     source_file_type = splitted_response[5].split("     ")
                     if ("Next startup saved-configuration file:" in source_file_type[0]):
                         source_file = source_file_type[1]
                     else:
                         raise Exception('huawei', 'Upload to remote server method: no source file for running!')

            else:
                raise Exception('huawei', 'Upload to remote server method: no source file for running!')

        return source_file

    def upload_to_remote_server(self, destination_file, configuration_type, vrf, timeout=600, retries=5):
        """Copy file from device to tftp or vice versa, as well as copying inside devices filesystem
        :param source_file: source file.
        :param destination_file: destination file.
        :return tuple(True or False, 'Success or Error message')
        """

        host = None

        if '://' in destination_file:
            destination_file_data_list = re.sub('/+', '/', destination_file).split('/')
            host = destination_file_data_list[1]
            filename = destination_file_data_list[-1]
        else:
            filename = destination_file
        print filename
        if host and not validateIP(host):
            raise Exception('huawei', 'Upload to remote server method: remote server ip is not valid!')

        source_file = self.get_configuration_file_name_from_device(configuration_type)
        tftp_command_str = 'tftp {0} put {1} {2}'.format(host, source_file, filename)


        expected_map = OrderedDict()
        if host:
            expected_map[host] = lambda session: session.send_line('')

        expected_map['\[Y/N\]'] = lambda session: session.send_line('y')
        expected_map['\(Y/N\)'] = lambda session: session.send_line('y')
        # expected_map['\(.*\)'] = lambda session: session.send_line('y')

        output = self.cli.send_command(command=tftp_command_str, expected_map=expected_map,check_action_loop_detector=False)

        return True,"Finished to save configuration"#self._check_download_from_tftp(output)

    def copy_configuration_inside_devices_filesystem(self, destination_file, configuration_type,vrf=None,check_action_loop_detector=False):

        """Copy file from device to tftp or vice versa, as well as copying inside devices filesystem
        :param source_file: source file.
        :param destination_file: destination file.
        :return tuple(True or False, 'Success or Error message')
        """
        is_success = True
        message = ''
        source_file = self.get_configuration_file_name_from_device(configuration_type)

        copy_commnd_str = 'copy %s %s' % (source_file, destination_file)
        expected_map = OrderedDict()
        expected_map['\[Y/N\]'] = lambda session: session.send_line('Y')
        expected_map['\(Y/N\)'] = lambda session: session.send_line('Y')
        output = self.cli.send_command(command=copy_commnd_str, expected_str='Done', expected_map=expected_map,check_action_loop_detector=check_action_loop_detector)
        error_match = re.search(r'(ERROR|[Ee]rror).*', output)
        if error_match:
            self.logger.error(error_match.group())
            is_success = False
            message = 'Copy completed with errors. Please see log for additional info.'

        return is_success, message

    def _check_download_from_tftp(self, output):
        """Verify if file was successfully uploaded by download th uploaded file form tftp
        :param output: output from cli
        :return True or False, and success or error message
        :rtype tuple
        """

        status_match = re.search(r'copied.*[\[\(].*[0-9]* bytes.*[\)\]]|[Cc]opy complete', output)
        is_success = (status_match is not None)
        message = 'Copy failed. Please see logs for additional info'
        if not is_success:
            match_error = re.search('%', output, re.IGNORECASE)
            if match_error:
                message = output[match_error.end():]
                message = message.split('\n')[0]

        error_match = re.search(r'(ERROR|[Ee]rror).*', output)
        if error_match:
            self.logger.error(error_match.group())
            if is_success is True:
                message = 'Copy completed with an errors. Please see logs for additional info'

        return is_success, message


    def reboot(self, sleep_timeout=60, retries=15,check_action_loop_detector=False):
        """Reload device

        :param sleep_timeout: period of time, to wait for device to get back online
        :param retries: amount of retires to get response from device after it will be rebooted
        """
        #,'Info: System is rebooting, please wait...':lambda a : time.sleep(250)
        expected_map = {'Continue\?\[Y/N\]': lambda session: session.send_line('y')}

        try:
            self.cli.send_command(command='reboot fast', expected_map=expected_map, timeout=3,check_action_loop_detector=check_action_loop_detector)


        except Exception as e:
            session_type = self.cli.get_session_type()

            if not session_type == 'CONSOLE':
                self.logger.info('Session type is \'{}\', closing session...'.format(session_type))
                self.cli.destroy_threaded_session()
                connection_manager = inject.instance(CONNECTION_MANAGER)
                connection_manager.decrement_sessions_count()


        self.logger.info('Wait 20 seconds for device to reload...')
        time.sleep(20)


        retry = 0
        is_reloaded = False
        while retry < retries:
            retry += 1

            time.sleep(sleep_timeout)
            try:
                self.logger.debug('Trying to send command to device ... (retry {} of {}'.format(retry, retries))
                output = self.cli.send_command(command='', expected_str='(?<![#\n])[#>] *$', expected_map={}, timeout=5,
                                               is_need_default_prompt=False)
                if len(output) == 0:
                    continue

                is_reloaded = True
                break
            except Exception as e:
                self.logger.error('HuaweiHandlerBase', 'Reload receives error: {0}'.format(e))
                self.logger.debug('Wait {} seconds and retry ...'.format(str(sleep_timeout / 2)))
                time.sleep(sleep_timeout / 2)
                pass

        return is_reloaded




    def update_firmware(self, remote_host, file_path, size_of_firmware=200000000):
        """Update firmware version on device by loading provided image, performs following steps (the steps are recommended by huawei Upgrade Guide):

            1. Copy .cc file from remote tftp server into the flash:/ dir.
            2. Clear un-served .cc files run from the device memory flash.
            3. Set downloaded bin file as boot file and then reboot device.
            4. Check if firmware was successfully installed.

        :param remote_host: host with firmware
        :param file_path: relative path on remote host
        :param size_of_firmware: size in bytes
        :return: status / exception
        """

        firmware_obj = HuaweiFirmwareData(file_path)
        if firmware_obj.get_name() is None:
            raise Exception('huawei VRP', "Invalid firmware name!\n \
                                Firmware file must have: title, extension.\n \
                                Example: S5700EIV100R006C01SPC112.CC\n\n \
                                Current path: " + file_path)


        src_file_name = file_path.split("/") if "/" in file_path else file_path.split("\\")
        if (len(src_file_name) > 0 and len(src_file_name) > 1): src_file_name = src_file_name[-1]
        else: raise Exception('huawei VRP', "Incorrect given file path%s"%(file_path))



        free_memory_size = self._get_free_memory_size('flash')

        response, dst_file = self.download_config_from_remote_server(source_file=remote_host, dst_path='flash:/' + src_file_name)



        expected_str="TFTP: Downloading the file successfully"
        if not re.search(expected_str, response, re.DOTALL):
            raise Exception('huawei VRP', "Failed to download firmware from " + remote_host +
                            file_path + "!\n" + dst_file)

        #self._remove_old_system_software_files()


        firmware_full_name = firmware_obj.get_name() + \
                             '.' + firmware_obj.get_extension()

        output = self.cli.send_command(command="startup system-software {0}".format(dst_file),expected_map={'Continue\?\[Y/N\]':lambda session: session.send_line('y')})
        bootrom_expected_str = "Info: Succeeded"
        if not re.search(bootrom_expected_str, output, re.DOTALL):
            raise Exception('huawei VRP', "Failed to upgrade firmware from " + remote_host +
                            file_path + "!\n" + dst_file)


        is_reloaded = self.reboot()

        if(is_reloaded == False):
            raise Exception('huawei VRP', "Failed to reload router after boot " + remote_host +
                            file_path + "!\n" + dst_file)


        output_version = self.cli.send_command(command='display version')

        is_firmware_installed = output_version.find(firmware_full_name)
        if is_firmware_installed != -1:
            return 'Finished updating firmware!'
        else:
            raise Exception('huawei VRP', 'Firmware update was unsuccessful!')

    def _get_free_memory_size(self, partition):
        """Get available memory size on provided partition
        :param partition: file system
        :return: size of free memory in bytes
        """

        cmd = 'dir {0}:'.format(partition)
        output = self.cli.send_command(command=cmd, retries=100)

        find_str = 'KB total ('
        position = output.find(find_str)
        if position != -1:
            size_str = output[(position + len(find_str)):]

            size_match = re.match('[0-9]*', size_str)
            if size_match:
                return int(size_match.group())
            else:
                return -1
        else:
            return -1

    def _get_resource_attribute(self, resource_full_path, attribute_name):
        """Get resource attribute by provided attribute_name

        :param resource_full_path: resource name or full name
        :param attribute_name: name of the attribute
        :return: attribute value
        :rtype: string
        """

        try:
            result = self.api.GetAttributeValue(resource_full_path, attribute_name).Value
        except Exception as e:
            raise Exception(e.message)
        return result

    def download_config_from_remote_server(self, source_file, dst_path):

        """The method goal is to download configuration file froma given remote path.
        :param folder_path:  tftp/ftp server where file be saved.
        :param dst_path: The destination inside the device where the file will be saved
        saved file name format: <ResourceName>-<ConfigurationType>-<DDMMYY>-<HHMMSS>
        :return: status message / exception and the saved file name
        """

        host = None

        if '://' in source_file:
            destination_file_data_list = re.sub('/+', '/', source_file.rstrip('/')).split('/')
            host = destination_file_data_list[1]
            if(destination_file_data_list[-2]!=host):
                filename = destination_file_data_list[-2] + '/' + destination_file_data_list[-1]
            else:
                filename =destination_file_data_list[-1]

        if host and not validateIP(host):
            raise Exception('huawei', 'Upload to remote server method: remote server ip is not valid!')
        dst_file = dst_path.strip("/") + "/" + destination_file_data_list[-1]
        tftp_command_str = 'tftp {0} get {1} {2}'.format(host, filename, dst_file)

        expected_map = OrderedDict()
        if host:
            expected_map[host] = lambda session: session.send_line('')

        expected_map['\[Y/N\]'] = lambda session: session.send_line('y')
        expected_map['\(Y/N\)'] = lambda session: session.send_line('y')

        output = self.cli.send_command(command=tftp_command_str, expected_map=expected_map,check_action_loop_detector=False)

        return output, dst_file

    def save_configuration(self, folder_path, configuration_type='', vrf=None,check_action_loop_detector=False):
        """Backup save the 'startup-config' or current 'running-config' from device to provided file_system [ftp|tftp]
        Also possible to backup config to the device
        :param folder_path:  tftp/ftp server where file be saved. Or a local path. tftp://<user>:<password>@<host>:<port>//<folder>
        :param configuration_type: Startup or Running
        saved file name format: <ResourceName>-<ConfigurationType>-<DDMMYY>-<HHMMSS>
        :return: status message / exception
        """
        remote = False
        if configuration_type == '':
            configuration_type = 'running'
        if (configuration_type.lower() != 'startup') and (configuration_type.lower() != 'running'):
            raise Exception('huawei failes during save configuration process',
                            "Source configuration type must be 'startup' or 'running'!")
        if folder_path == '':
            folder_path = self._get_resource_attribute(self.resource_name, 'Backup Location')
            if len(folder_path) <= 0:
                raise Exception('huawei failes during save configuration process', "Path is empty")

        system_name = re.sub('\s+', '_', self.resource_name)
        if len(system_name) > 23:
            system_name = system_name[:23]

        destination_filename = '{0}-{1}-{2}.zip'.format(system_name, configuration_type.lower(),
                                                    _get_time_stamp())
        self.logger.info('configuration destination filename is {0}'.format(destination_filename))
        if folder_path.startswith('ftp://') or folder_path.startswith('tftp://'): remote = True


        destination_file = folder_path.rstrip('/') + '/' + destination_filename

        if remote: is_uploaded = self.upload_to_remote_server(destination_file=destination_file,
                                                              configuration_type=configuration_type, vrf=vrf)

        if remote == False: is_uploaded = self.copy_configuration_inside_devices_filesystem(
            destination_file=destination_file, configuration_type=configuration_type, vrf=vrf)


        if is_uploaded[0] is True:
            self.logger.info('Save complete')
            return '{0}'.format(destination_filename)
        else:
            self.logger.info('Save failed with an error: {0}'.format(is_uploaded[1]))
            raise Exception(is_uploaded[1])

    def restore_configuration(self, source_path, configuration_type, restore_method='override', vrf=None):
        """Restore configuration on device from provided configuration file
        Restore configuration from local file system or ftp/tftp server into 'running-config' or 'startup-config'.
        :param source_file: relative path to the file on the remote host tftp://server/sourcefile
        :param restore_method: override current config or not
        :return:
        """
        if re.search('append',restore_method.lower()):
            raise Exception('huawei',"huawei do no yet support append operations on configuration files")
        if not re.search('override', restore_method.lower()):
            raise Exception('huawei', "Restore method is wrong! Should be Append or Override")

        if (configuration_type.lower() != 'startup') and (configuration_type.lower() != 'running'):
            raise Exception('huawei failes during save configuration process',
                            "Source configuration type must be 'startup' or 'running'!")

        self.logger.info('Start restoring device configuration from {}'.format(source_path))

        match_data = re.search('startup|running', configuration_type.lower())
        if not match_data:
            raise Exception('huawei', "Configuration type is empty or wrong")

        if source_path == '': raise Exception('huawei', "Path is empty")

        remote = False

        if '://' in source_path:
            remote = True
            dst_path = self.cli.send_command(command='pwd')
            if (dst_path != ''): dst_path = dst_path.strip('pwd\n').split('\n\n')
            if (len(dst_path) > 0): dst_path = dst_path[0]
            if (not dst_path.endswith('/')): dst_path = dst_path + '/'

        if (remote): output, source_path = self.download_config_from_remote_server(source_path, dst_path)

        if (restore_method.lower() == 'override') and (configuration_type.lower() == 'startup' or configuration_type.lower() == 'running'):
            command = 'display startup'
            response = self.cli.send_command(command=command)
            splitted_response = response.split("\n  ")
            if (len(splitted_response) <= 0): raise Exception('huawei',
                                                              'copy configuration inside devices filesystem method: no source file for startup!')

            startup_source_file_name = splitted_response[5].split("     ")
            if (len(startup_source_file_name) <= 0): raise Exception('huawei',
                                                                     'copy configuration inside devices filesystem method: no source file for startup!')
            if ("Next startup saved-configuration file:" in startup_source_file_name[0]):
                startup_source_file = startup_source_file_name[1]
            else:
                raise Exception('huawei',
                                'copy configuration inside devices filesystem method: no source file for startup!')
            expected_map = OrderedDict()
            expected_map[r'\[Y/N\]'] = lambda session: session.send_line('y')

            self.cli.send_command(command='copy {0} {1}'.format(source_path, startup_source_file),
                                  expected_map=expected_map,check_action_loop_detector=False)

        if (restore_method.lower() == 'override') and (configuration_type.lower() == 'running'):
            is_reloaded = self.reboot()

            if (is_reloaded == False):
                raise Exception('huawei VRP', "Failed During Reseting Current Configuration")

        return 'Finished restore configuration!'


