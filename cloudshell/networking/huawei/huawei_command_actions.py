import re
from cloudshell.cli.cli_exception import CliException
from cloudshell.networking.huawei.command_templates.huawei_configure_vlan_template import *
from cloudshell.networking.huawei.command_templates.huawei_commands_templates import *



def install_firmware(config_session, logger, firmware_file_name):
    """Set boot firmware file.
    :param config_session: current config session
    :param logger:  logger
    :param firmware_file_name: firmware file name
    """
    config_session.send_command(**UPDATE_FIRMWARE.get_command(firmware_file_name))


def create_vlan(session, logger, vlan_range, action_map=None, error_map=None):
    """Create vlan entity on the device

    :param session: current session
    :param logger:  logger
    :param vlan_range: range of vlans to be created
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    """
    ranges_list = []
    is_range = True if '-' in vlan_range else False
    splited_vlan_range = vlan_range.split(',')

    if (len(splited_vlan_range) > 1) or is_range:
        for vlan in splited_vlan_range:

            if '-' in vlan:
                ranges_leafs = vlan.split('-')

                if (int(ranges_leafs[0]) > int(ranges_leafs[1])):
                    temp = ranges_leafs[0]
                    ranges_leafs[0] = ranges_leafs[1]
                    ranges_leafs[1] = temp

                ranges_list = ranges_list + (range(int(ranges_leafs[0]), int(ranges_leafs[1]) + 1))
            else:
                ranges_list.append(vlan)

            session.send_command(**VLAN_BATCH.get_command(vlan_id=ranges_leafs[0] + " to " + ranges_leafs[1],
                                                              action_map=action_map,
                                                              error_map=error_map))
    else:
        session.send_command(**CONFIGURE_VLAN.get_command(vlan_id=vlan_range,
                                                          action_map=action_map,
                                                          error_map=error_map))

def set_vlan_to_interface(config_session, logger, vlan_range, port_mode, port_name, qnq, c_tag,
                          action_map=None,
                          error_map=None):
    """Assign vlan to a certain interface

    :param config_session: current config session
    :param logger:  logger
    :param vlan_range: range of vlans to be assigned
    :param port_mode: switchport mode
    :param port_name: interface name
    :param qnq: qinq settings (dot1q tunnel)
    :param c_tag: selective qnq
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    """

    curr_config = get_current_interface_config(config_session,port_name)
    config_session.send_command(**CONFIGURE_INTERFACE.get_command(port_name=port_name))
    clean_current_configuration_on_interface(config_session, logger, curr_config, port_name, action_map=None,
                                             error_map=None)

    config_session.send_command(**UNDO_SHUTDOWN.get_command(action_map=action_map, error_map=error_map))
    config_session.send_command(**START_PORT_MODE.get_command(action_map=action_map, error_map=error_map))

    is_range = True if '-' in vlan_range else False

    if port_mode == 'trunk':
        if (is_range):
            splited_vlan_range = vlan_range.split(',')

            if (len(splited_vlan_range) > 1) or is_range:
                for vlan in splited_vlan_range:

                    if '-' in vlan:
                        ranges_leafs = vlan.split('-')

                        if (int(ranges_leafs[0]) > int(ranges_leafs[1])):
                            temp = ranges_leafs[0]
                            ranges_leafs[0] = ranges_leafs[1]
                            ranges_leafs[1] = temp

                        ranges_list = ranges_list + (range(int(ranges_leafs[0]), int(ranges_leafs[1]) + 1))
                    else:
                        ranges_list.append(vlan)

                        config_session.send_command(**ALLOW_TRUNK_VLAN.get_command(vlan_id=ranges_leafs[0] + " to " + ranges_leafs[1],
                                                                  action_map=action_map,
                                                                  error_map=error_map))

        else:
            config_session.send_command(
                **ALLOW_TRUNK_VLAN.get_command(vlan_id=vlan_range,
                                               action_map=action_map,
                                               error_map=error_map))
    elif 'access' in port_mode and vlan_range != '':
        if not qnq or qnq is False:
            logger.info('qnq is {0}'.format(qnq))
            config_session.send_command(
                **PORT_MODE_ACCESS.get_command(vlan_id=vlan_range,
                                               action_map=action_map,
                                               error_map=error_map))
            config_session.send_command(
                **PORT_DEFAULT_VLAN.get_command(vlan_id=vlan_range,
                                               action_map=action_map,
                                               error_map=error_map))

    if qnq and qnq is True:
        config_session.send_command(
            **QNQ.get_command(vlan_id=vlan_range,
                                            action_map=action_map,
                                            error_map=error_map))
        config_session.send_command(
            **PORT_DEFAULT_VLAN.get_command(vlan_id=vlan_range,
                                            action_map=action_map,
                                            error_map=error_map))

    config_session.send_command(
        **COMMIT.get_command(action_map=action_map,
                                        error_map=error_map))

    logger.info('Vlan configuration completed\n')

def clean_current_configuration_on_interface(config_session, logger, current_config, port_name, action_map=None,
                                      error_map=None):

        """

        :param :
        :return: success message
        :rtype: string
        """
        line_to_remove = None
        action_map = {'[\[\(][Yy]es/[Nn]o[\)\]]|\[Continue\]|Continue?\[Y/N\]': lambda session: session.send_line('yes'),
                        '[\[\(][Yy]/[Nn][\)\]]': lambda session: session.send_line('y')}
        for line in current_config.splitlines():
            if re.search('^\s*port default vlan\s+|^\s*port link-type\s+|^\s*port trunk allow-pass vlan\s+', line):
                if(not re.search('^\s*port trunk allow-pass vlan\s+', line)):
                    line_to_remove = re.sub('\s+\d+[-\d+,]+|trunk|access', '', line)
                if not line_to_remove:
                    line_to_remove = line

                config_session.send_command(
                    **UNDO.get_command(command=line_to_remove, action_map=action_map, error_map=error_map))

        return 'Finished configuration of ethernet interface!'

def reboot(session, logger):
    """Reload device

    :param session: current session
    :param logger:  logger
    :param timeout: session reconnect timeout
    """

    """Reload device

     :param sleep_timeout: period of time, to wait for device to get back online
     :param retries: amount of retires to get response from device after it will be rebooted
     """
    # ,'Info: System is rebooting, please wait...':lambda a : time.sleep(250)

    try:
        session.send_command(
            **REBOOT.get_command())
    except Exception as e:
        logger.info("Device rebooted, starting reconnect")




def save_configuration(session, logger, configuration_type, destination, vrf=None, action_map=None, error_map=None):
    """Save file from device to tftp or vice versa, as well as copying inside devices filesystem.

    :param session: current session 
    :param logger:  logger
    :param source: source file
    :param destination: destination file
    :param vrf: vrf management name
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    :raise Exception: 
    """

    if not vrf:
        vrf = None
    remote = False

    destination_filename = destination
    logger.info('configuration destination filename is {0}'.format(destination_filename))
    if destination.startswith('ftp://') or destination.startswith('tftp://'): remote = True


    if remote: output = upload_to_remote_server(session=session,destination_file=destination_filename,
                                                          configuration_type=configuration_type, vrf=vrf)


    if remote == False: output = copy_configuration_inside_devices_filesystem(
        session=session,destination_file=destination_filename, configuration_type=configuration_type, vrf=vrf)

    status_match = re.search(r'\d+ bytes copied|copied.*[\[\(].*[0-9]* bytes.*[\)\]]|[Cc]opy complete', output,
                             re.IGNORECASE)
    if not status_match:
        match_error = re.search('%.*|TFTP put operation failed.*|sysmgr.*not supported.*\n', output, re.IGNORECASE)
        message = 'Save Command failed. '
        if match_error:
            logger.error(message)
            message += re.sub('^%|\\n', '', match_error.group())
        else:
            error_match = re.search(r"error.*\n|fail.*\n", output, re.IGNORECASE)
            if error_match:
                logger.error(message)
                message += error_match.group()
        raise Exception('Save Operation', message)

def copy_configuration_inside_devices_filesystem(session,destination_file, configuration_type,vrf=None):

    """Copy file from device to tftp or vice versa, as well as copying inside devices filesystem
    :param source_file: source file.
    :param destination_file: destination file.
    :return tuple(True or False, 'Success or Error message')
    """
    is_success = True
    message = ''
    source_file = get_configuration_file_name_from_device(configuration_type)

    output = session.send_command(
        **COPY.get_command(src=source_file, dst=destination_file))

    return output

def upload_to_remote_server(session,destination_file, configuration_type,vrf):

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

    source_file = get_configuration_file_name_from_device(session,configuration_type)

    output = session.send_command(
        **TFTP_PUT.get_command(host=host,src=source_file, dst=filename))

    return output

def get_configuration_file_name_from_device(session,configuration_type):

    response = session.send_command(**DISPLAY_STARTUP.get_command())

    if (configuration_type == 'startup'):
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


def restore_configuration(session, logger,source_path, configuration_type, action_map,restore_method='override', vrf=None):
        """Restore configuration on device from provided configuration file
        Restore configuration from local file system or ftp/tftp server into 'running-config' or 'startup-config'.
        :param source_file: relative path to the file on the remote host tftp://server/sourcefile
        :param restore_method: override current config or not
        :return:
        """

        remote = False

        if '://' in source_path:
            remote = True
            dst_path = session.send_command(**PWD.get_command())
            if (dst_path != ''): dst_path = dst_path.strip('pwd\n').split('\n\n')
            if (len(dst_path) > 0): dst_path = dst_path[0]
            if (not dst_path.endswith('/')): dst_path = dst_path + '/'

        if (remote): output, source_path = download_config_from_remote_server(session,source_path, dst_path)

        if (restore_method.lower() == 'override') and (configuration_type.lower() == 'startup' or configuration_type.lower() == 'running'):

            response = session.send_command(**DISPLAY_STARTUP.get_command())
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

            output = session.send_command(
                **COPY.get_command(src=source_path, dst=startup_source_file))

        if (restore_method.lower() == 'override') and (configuration_type.lower() == 'running'):
            reboot(session, logger)

        return output

def download_config_from_remote_server(session, source_file, dst_path):

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

    dst_file = dst_path.strip("/") + "/" + destination_file_data_list[-1]
    output = session.send_command(
        **TFTP_GET.get_command(host=host,src=source_file, dst=filename))

    return output, dst_file

def get_current_interface_config(config_session,port_name, action_map=None, error_map=None):
    """Retrieve current interface configuration

    :param session: current session 
    :param logger:  logger
    :param port_name: 
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    :return: str
    """

    return config_session.send_command(
        **DISPLAY_RUNNING.get_command(port_name=port_name, action_map=action_map, error_map=error_map))

def update_firmware(session, file_path,firmware_name,logger):
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

        src_file_name = file_path.split("/") if "/" in file_path else file_path.split("\\")
        if (len(src_file_name) > 0 and len(src_file_name) > 1): src_file_name = src_file_name[-1]
        else: raise Exception('huawei VRP', "Incorrect given file path%s"%(file_path))

        response, dst_file = download_config_from_remote_server(source_file=file_path, dst_path='flash:/' + src_file_name)

        expected_str="TFTP: Downloading the file successfully"
        if not re.search(expected_str, response, re.DOTALL):
            raise Exception('huawei VRP', "Failed to download firmware from " + file_path +
                            file_path + "!\n" + dst_file)

        output = session.send_command(
        **STARTUP_SYSTEM_SOFTWARE.get_command(dst_file=dst_file))
        bootrom_expected_str = "Info: Succeeded"
        if not re.search(bootrom_expected_str, output, re.DOTALL):
            raise Exception('huawei VRP', "Failed to upgrade firmware from " + file_path +
                            file_path + "!\n" + dst_file)

        is_reloaded = reboot(session,logger)

        if(is_reloaded == False):
            raise Exception('huawei VRP', "Failed to reload router after boot " + file_path +
                            file_path + "!\n" + dst_file)



        output_version = session.send_command(
        **DISPLAY_VERSION.get_command(dst_file=dst_file))
        is_firmware_installed = output_version.find(firmware_name)
        if is_firmware_installed != -1:
            return 'Finished updating firmware!'
        else:
            raise Exception('huawei VRP', 'Firmware update was unsuccessful!')


def get_current_os_version(session, action_map=None, error_map=None):
    """Retrieve os version

    :param session: current session 
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    :return: 
    """

    return session.send_command(**DISPLAY_VERSION.get_command(action_map=action_map, error_map=error_map))


def get_current_boot_config(session, action_map=None, error_map=None):
    """Retrieve current boot configuration

    :param session: current session
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    :return:
    """

    return session.send_command(**DISPLAY_RUNNING.get_command(boot='', action_map=action_map, error_map=error_map))




def verify_interface_configured(vlan_range, current_config):
    """Verify interface configuration

    :param vlan_range: 
    :param current_config: 
    :return: True or False
    """

    return str(vlan_range) in current_config


def enable_snmp(session, snmp_community, action_map=None, error_map=None):
    """Enable SNMP on the device

    :param session: current session 
    :param snmp_community: community name
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    """
    session.send_command(**SNMP_ENABLE.get_command(action_map=action_map, error_map=error_map))


def disable_snmp(session, snmp_community, action_map=None, error_map=None):
    """Disable SNMP on the device

    :param session: current session 
    :param snmp_community: community name
    :param action_map: actions will be taken during executing commands, i.e. handles yes/no prompts
    :param error_map: errors will be raised during executing commands, i.e. handles Invalid Commands errors
    """
    session.send_command(**SNMP_DISABLE.get_command(action_map=action_map, error_map=error_map))


def get_port_name(logger, port):
    """Get port name from port resource full address

    :param port: port resource full address (192.168.1.1/0/34)
    :return: port name (FastEthernet0/23)
    :rtype: string
    """

    if not port:
        err_msg = 'Failed to get port name.'
        logger.error(err_msg)
        raise Exception('HuaweiConnectivityOperations: get_port_name', err_msg)

    temp_port_name = port.split('/')[-1]
    if 'port-channel' not in temp_port_name.lower():
        temp_port_name = temp_port_name.replace('-', '/')

    logger.info('Interface name validation OK, portname = {0}'.format(temp_port_name))
    return temp_port_name
