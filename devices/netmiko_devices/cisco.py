# Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from networking_generic_switch.devices import netmiko_devices


class CiscoIos(netmiko_devices.NetmikoSwitch):
        ADD_NETWORK = (
            'vlan {segmentation_id}',
            'name {network_id}',
        )

        DELETE_NETWORK = (
            'no vlan {segmentation_id}',
        )

        PLUG_PORT_TO_NETWORK = (
            'interface {port}',
            'switchport mode access',
            'switchport access vlan {segmentation_id}',
        )

        DELETE_PORT = (
            'interface {port}',
            'no switchport access vlan {segmentation_id}',
            'no switchport mode trunk',
            'switchport trunk allowed vlan none'
        )

        SAVE_CONFIGURATION = (
            'write memory'
        )
        
        CREATE_PORT_CHANNEL = (
            'interface {port_channel_id}',
        )

        CONFIGURE_PORT = (
            'interface {port}',
            'no shutdown',
            'channel-group {port_channel_id} mode on'
        )
        
        SHOW_PORT_LIST = (
            'show run | inc Port-channel'
        )
