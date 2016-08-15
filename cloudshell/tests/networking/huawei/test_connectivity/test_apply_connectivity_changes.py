__author__ = 'Luiza Nacshon'
from unittest import TestCase
from mock import MagicMock
from cloudshell.networking.huawei.huawei_connectivity_operations import HuaweiConnectivityOperations
from cloudshell.networking.generic_bootstrap import NetworkingGenericBootstrap
import cloudshell.networking.huawei.vrp.huawei_vrp_configuration as driver_config
import re


class TestHuaweiConnectivity(TestCase):


    def _get_handler(self):
        bootstrap = NetworkingGenericBootstrap()
        bootstrap.add_config(driver_config)
        bootstrap.initialize()
        self.cli = MagicMock()
        self.snmp = MagicMock()
        self.api = MagicMock()
        self.logger = MagicMock()
        return HuaweiConnectivityOperations(cli=self.cli, logger=self.logger, api=self.api,
                                            resource_name='Huawei37')

    def test_apply_connectivity_changes_validates_request_parameter(self):

        request = """{
        	"driverRequest": {
        		"actions": [{
        			"connectionId": "8ccac528-2ff9-4b6d-9415-9dd68ac390c6",
        			"connectionParams": {
        				"vlanId": "23",
        				"mode": "Access",
        				"vlanServiceAttributes": [{
        					"attributeName": "QnQ",
        					"attributeValue": "False",
        					"type": "vlanServiceAttribute"
        				}, {
        					"attributeName": "CTag",
        					"attributeValue": "",
        					"type": "vlanServiceAttribute"
        				}, {
        					"attributeName": "Isolation Level",
        					"attributeValue": "Shared",
        					"type": "vlanServiceAttribute"
        				}, {
        					"attributeName": "Access Mode",
        					"attributeValue": "Access",
        					"type": "vlanServiceAttribute"
        				}, {
        					"attributeName": "VLAN ID",
        					"attributeValue": "23",
        					"type": "vlanServiceAttribute"
        				}, {
        					"attributeName": "Pool Name",
        					"attributeValue": "",
        					"type": "vlanServiceAttribute"
        				}, {
        					"attributeName": "Virtual Network",
        					"attributeValue": "23",
        					"type": "vlanServiceAttribute"
        				}],
        				"type": "setVlanParameter"
        			},
        			"connectorAttributes": [],
        			"actionId": "8ccac528-2ff9-4b6d-9415-9dd68ac390c6_ef6ea31d-40fc-4044-ae80-82fa74dfa695",
        			"actionTarget": {
        				"fullName": "Huawei37/Chassis 1/Module 0/GigabitEthernet0-0-1",
        				"fullAddress": "172.19.0.37/1/0/1",
        				"type": "actionTarget"
        			},
        			"customActionAttributes": [],
        			"type": "setVlan"
        		}]
        	}
        }"""


        assert_response = {"driverResponse": {"actionResults": [{"success": False, "updatedInterface": "Huawei37/Chassis 1/Module 0/GigabitEthernet0-0-1", "errorMessage": "expected string or buffer", "infoMessage": "null", "actionId": "8ccac528-2ff9-4b6d-9415-9dd68ac390c6_ef6ea31d-40fc-4044-ae80-82fa74dfa695", "type": "setVlan"}]}}

        handler = self._get_handler()
        handler.cli.send_command = MagicMock(return_value="vlan added")
        handler.get_port_name = MagicMock(return_value='GigabitEthernet0-0-1')
        response = handler.apply_connectivity_changes(request)
        self.assertIsNotNone(response)
        self.assertTrue(re.search( "Huawei37/Chassis 1/Module 0/GigabitEthernet0-0-1", response))