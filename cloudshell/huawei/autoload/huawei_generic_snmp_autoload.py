#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.snmp.autoload.generic_snmp_autoload import (
    GeneralAutoloadError,
    GenericSNMPAutoload,
    log_autoload_details,
)


class HuaweiGenericSNMPAutoload(GenericSNMPAutoload):
    def __init__(self, snmp_handler, logger):
        super(HuaweiGenericSNMPAutoload, self).__init__(snmp_handler, logger)

    def discover(
        self, supported_os, resource_model, validate_module_id_by_port_name=False
    ):
        """General entry point for autoload.

        Read device structure and attributes: chassis, modules, submodules, ports,
        port-channels and power supplies
        :type resource_model: cloudshell.shell.standards.autoload_generic_models.GenericResourceModel  # noqa: E501
        :param str supported_os:
        :param bool validate_module_id_by_port_name:
        :return: AutoLoadDetails object
        """
        self.entity_table_service.validate_module_id_by_port_name = (
            validate_module_id_by_port_name
        )
        if not resource_model:
            return
        self._resource_model = resource_model
        if not self.system_info_service.is_valid_device_os(supported_os):
            raise GeneralAutoloadError("Unsupported device OS")

        self.logger.info("*" * 70)
        self.logger.info("Start SNMP discovery process .....")
        self.system_info_service.fill_attributes(resource_model)

        entity_chassis_tree_dict = self.entity_table_service.chassis_structure_dict

        if entity_chassis_tree_dict:
            self._build_structure(entity_chassis_tree_dict.values(), resource_model)
            self._get_port_channels(resource_model)

        autoload_details = resource_model.build(
            filter_empty_modules=True, use_new_unique_id=True
        )

        log_autoload_details(self.logger, autoload_details)
        return autoload_details
